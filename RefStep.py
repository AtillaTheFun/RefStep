"""
Main thread for controlling the buttons of the ref-step algorithm.
Information is collected here and sent to other objects for handling. 
"""
import wx, wx.html
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import GTC
import csv
import os
import sys
import visa
import time
import PyPDF2
import docx

import modules.noname as noname
import modules.visa2 as visa2 # this is the simulation version of visa
import modules.GridMaker as GridMaker
import modules.pywxgrideditmixin as pywxgrideditmixin
import modules.tables as tables
import modules.analysis as analysis
import modules.gpib_data as gpib_data
import modules.gpib_inst as gpib_inst
import modules.stuff as stuff
import modules.ReportBuilder as ReportBuilder
class GraphFrame(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        #the mixin below offers better ctrl c ctr v cut and paste than the basic wxgrid
        wx.grid.Grid.__bases__ += (pywxgrideditmixin.PyWXGridEditMixin,)
        self.m_grid3.__init_mixin__()
        self.m_grid21.__init_mixin__()
        self.m_grid2.__init_mixin__()
        self.m_grid4.__init_mixin__()
#        self.m_grid8.__init_mixin__()
        
        self.number_plots = 1
        self.ranges=[]
        
        self.paused = True
        self.Show(True)
        self.Validate = False
        self.EVT_RESULT_ID_1 = wx.NewId() #used for GPIB data 1 thread

        self.worker1 = None # for data source 1
        stuff.EVT_RESULT(self, self.OnResult1, self.EVT_RESULT_ID_1)
        log = self.m_textCtrl81 # where stdout will be redirected
        redir = stuff.RedirectText(log)
        sys.stdout = redir #print statements, note to avoid 'print' if callafter delay is an issue
        sys.stderr = redir #python errors
        self.data = stuff.SharedList(None) #no data on start up

        self.cwd = os.getcwd() #identifies working directory at startup.
        iconFile = os.path.join(self.cwd, 'testpoint.ico')
        icon1 = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)
        self.dirname = 'xxx'
        self.SetIcon(icon1)
        self.inst_bus = visa # can be toggled (OnSimulate) to visa 2 for simulation
        self.START_TIME = 0 #to be overidden when worker thread is called
        self.filled_grid = False #was grid sucessfuly filled
        self.loaded_dict = False
        self.loaded_ranges = False
        self.OverideSafety = False

        
        col_names = ['Min','Max','# Readings','Pre-reading delay','Inter-reading delay','# Repetitions','# steps']
        for i in range(len(col_names)):
            self.m_grid21.SetColLabelValue(i, col_names[i])
            
        #Murray wanted a popup window with info?
        self.OnAbout(None)
        
    def OnCreateReport(self, event):
        
        """
        Uses the Report builder to output a Calibration Report.
        """

        CalRep = ReportBuilder.CalReport()
        CalRep.init(self)
        CalRep.BuildReport()
        
    def OnSource(self, event):

        """
        Respond to checkbox events.
        """

        if self.m_checkBox1.GetValue():
            self.m_checkBox1.SetValue(False)
        else:
            self.m_checkBox1.SetValue(True)
    
    def OnMeter(self, event):

        """
        Respond to checkbox events.
        """

        if self.m_checkBox2.GetValue():
            self.m_checkBox2.SetValue(False)
        else:
            self.m_checkBox2.SetValue(True)
            
    def dcStop(self, event):

        """
        Flags the worker thread to stop running if it exists.
        """

        # Flag the worker thread to stop if running
        if self.worker1:
            print('Halting GPIB data gathering')
            self.worker1.abort() 
        
    def dcStart(self, event):

        """
        Creates the instruments, and calls the doStart function. 
        """

        log = self.m_textCtrl91 # where stdout will be redirected
        redir = stuff.RedirectText(log)
        sys.stdout = redir #print statements, note to avoid 'print' if callafter delay is an issue
        sys.stderr = redir #python errors
        if self.filled_grid == True:
            instruments = self.dcCreateMeter()
            self.dcDoStart(instruments)
        else:

            print("Input grids changed, generate a table again to continue")
        
        
    def dcMakeSafe(self, event):

        """
        Flags all threads to stop.
        """

        if self.worker1:
            self.worker1.MakeSafe()
        self.doStop() #stop main data gathering
        self.paused = True 
        #self.m_button2.SetLabel("Plot")

       
        
    def dcCreateMeter(self):

        """
        Reads the dictionary uploaded to the grid, and creates gpib_inst.INSTRUMENT accordingly.
        Instruments must be the meter on the left, source S in the middle, source X on the right.
        """

        def sim(s):

            """Nested function used only here, returns a simplified string"""

            s = s.replace('\\r','\r')
            s = s.replace('\\n','\n')
            #Other simplifications might be necessary in the future I suppose.
            return s
        
        dicts = self.m_grid2
        dm={} #Meter dictionary
        dx={} #X dictionary
        ds={} #S dictionary
        rows = dicts.GetNumberRows()
        for row in range(rows):
            dm.update({sim(dicts.GetCellValue(row, 0)):sim(dicts.GetCellValue(row, 1))})
            ds.update({sim(dicts.GetCellValue(row, 2)):sim(dicts.GetCellValue(row, 3))})
            dx.update({sim(dicts.GetCellValue(row, 4)):sim(dicts.GetCellValue(row, 5))})
        #Unpack the dictionaries to each respective instrument.
        self.meter = gpib_inst.INSTRUMENT(self.inst_bus, 'M', address=self.Meteraddress.GetValue(), **dm)
        return [self.meter]
        
    def dcDoStart(self, instruments):

        """
        Starts the algorithm, sends the created instruments to the wroker thread.
        """
        
        self.meter = instruments[0]
        #first read essential setup info from the control grid (self.m_grid3).        
        grid = self.m_grid91
        grid.EnableEditing(False)
        #int(float()) is needed because the grid has loaded,e.g. 2.0 instead of 2
        
        dvm_range_col = 0
        
        self.START_TIME = time.localtime()
        
        #DISABLE BUTTONS
        for button in [self.m_menuItem21,self.m_menuItem11,self.m_menuItem111,\
                       self.m_menuItem2,self.m_menuItem1,self.m_menuItem25,\
                       self.m_menuItem26,self.m_button15,self.m_button16]:
            button.Enable(False)
        
        
        #now call the thread
        if not self.worker1:
            self.worker1 = gpib_data.GPIBThreadDC(self, self.EVT_RESULT_ID_1,\
            [self.inst_bus, grid, self.meter,\
             dvm_range_col, self.Analysis_file_name,self.m_textCtrl92.GetValue(),self.m_textCtrl93.GetValue()],\
            self.data,self.START_TIME,self.OverideSafety,self)
            #It has a huge list of useful things that it needs.

    def OnAddRowDC(self,event):

        """Add another row to the ranges table, this is necessary as it requires manual inputting."""

        self.m_grid91.AppendRows(1, True)
        self.m_grid91.Layout()

            
    def OnOpenData(self, event):

        """
        from MIEcalculator, graph_gui.py.
        """

        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a data file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)

        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.data_file = os.path.join(dirname, filename)
            #remember the project working directory
            self.FillData()
        self.m_textCtrl187.Clear() 
        self.m_textCtrl187.WriteText(filename) # update text field with current data file. 
        dlg.Destroy()

    def OnOpenDCData(self, event):

        """
        from MIEcalculator, graph_gui.py.
        """

        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a data file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)

        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.DCdata_file = os.path.join(dirname, filename)
            self.FillDCData()
        self.m_textCtrl187b.Clear() 
        self.m_textCtrl187b.WriteText(filename) # update text field with current data file. 
        dlg.Destroy()
        
    def FillData(self):

        """
        Loads data to create a report. Requires a results sheet named "Results".
        Uses tables.TABLES for a excel-to-grid object.
        """
        
        datagrid = tables.TABLES(self)
        self.data_grid = datagrid.excel_to_grid(self.data_file, 'Results', self.m_grid44)
        self.data_grid = datagrid.excel_to_grid(self.data_file, 'Gain Ratios', self.m_grid42) 
        self.data_grid = datagrid.excel_to_grid(self.data_file, 'Linearity Ratios', self.m_grid43)
        meter_row = 0
        for i in range(0, self.m_grid42.GetNumberRows()):
            if self.m_grid42.GetCellValue(i,0) == 'Meter Gain Ratios' :
                meter_row = i
        if self.m_checkBox1.GetValue():
            self.m_grid42.DeleteRows(0,meter_row)
            
            
        else:
            self.m_grid42.DeleteRows(meter_row-1, self.m_grid42.GetNumberRows()-1)
            
            
    def FillDCData(self):

        """
        Loads data to create a report. Requires a results sheet named "Results".
        Uses tables.TABLES for a excel-to-grid object.
        """
        
        datagrid = tables.TABLES(self)
        self.data_grid = datagrid.excel_to_grid(self.DCdata_file, 'Sheet', self.m_grid41)
        
    def OnChooseAnalysisFile(self, event):  
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a data file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)

        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
        self.Analysis_file_name.Clear() 
        self.Analysis_file_name.WriteText(filename) # update text field with current data file. 
        dlg.Destroy()
        
    def OnClearResultsDC(self, event):

        """
        Clears the Calibration Ranges table in the DC Offset Measurement tab to allow additional test runs. 
        Reloads the ranges into the table once it is clear.
        """

        self.m_grid91.ClearGrid()
        print('Clear Grid')
        self.FillGrid()
        
    def OnLive(self, event):

        """
        Chooses visa for live instruments
        """

        if self.m_menuItem2.IsChecked():
            self.inst_bus = visa #default for real instruments        
        
    def OnSimulate(self, event):

        """
        Chooses visa2 for simulated (poorly) GPIB.
        """

        if self.m_menuItem1.IsChecked():
            self.inst_bus = visa2 #choose visa2 for simulation
        else:
            self.inst_bus = visa

    def OnOpenDict(self, event):

        """
        from MIEcalculator, graph_gui.py.
        """

        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a project file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)

        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.proj_file = os.path.join(dirname, filename)
            self.projwd = dirname #remember the project working directory
            
        dlg.Destroy()
        
        
        
        self.FillGrid()
        
    def OnLoadTable(self, event):

        """Immediatly  calls the FillGrid function, so it can be used without the event too."""

        self.FillGrid()
        
    def FillGrid(self):

        """
        Loads self.proj_file to the grid. Requires a dictionary sheet named "Dict" and
        a control sheet named "Sheet 1". Uses tables.TABLES for a excel-to-grid object.
        """
        
        controlgrid = tables.TABLES(self)

        self.filled_grid = controlgrid.excel_to_grid(self.proj_file, 'Control', self.m_grid3)
        if self.filled_grid == True:
            grid = self.m_grid3
            if int(float(grid.GetCellValue(3,3)))>int(grid.GetNumberRows()):
                #int(float(is needed as it cant seem to cast straight to an int
                print("Final row needed to be updated in grid")
                grid.SetCellValue(3,3,str(grid.GetNumberRows()))
            self.m_grid3.Layout()
        else:
            print("no sheet named 'Control' found")
            
        self.loaded_dict = controlgrid.excel_to_grid(self.proj_file, 'Dict', self.m_grid2)
        if self.loaded_dict == True:
            col_names = ['Key words','Meter','Key words','Source S','Key words','Source X']
            for i in range(len(col_names)):
                self.m_grid2.SetColLabelValue(i, col_names[i])
            self.m_grid2.Layout()
            
            
        else:
            print("no sheet named 'Dict' found, can not run")
            
        self.loaded_ranges = controlgrid.excel_to_grid(self.proj_file, 'Ranges', self.m_grid21)
        
        if self.loaded_ranges == True:
            
            col_names = ['Min','Max','# Readings','Pre-reading delay','Inter-reading delay','# Repetitions','# steps']
            for i in range(len(col_names)):
                self.m_grid21.SetColLabelValue(i, col_names[i])
            self.m_grid21.Layout()                       
            #Copy ranges from m_grid21 to m_grid91
            rows = self.m_grid21.GetNumberRows()
            rows = range(0,int(rows))
            for x in rows:
                self.m_grid91.SetCellValue(x+1,0, self.m_grid21.GetCellValue(x,1))
        else:
            print("no sheet named 'Ranges' found")
            
                    #wip
        i = 0
        while(isinstance(self.m_grid21.GetCellValue(1,i), (int, long, float))):
            self.m_grid91.SetCellValue(0,i,self.m_grid21.GetCellValue(1,i)) 
            i = i+1
                

    def OnAddRow(self,event):

        """Add another row to the ranges table, this is necessary as it requires manual inputting."""

        self.m_grid21.AppendRows(1, True)
        self.m_grid21.Layout()
        
    def OnAddRange(self,event):

        """Add a range to the Calibration Ranges table """

        ranges = self.m_grid21.GetNumberRows()
        i = 0
        while i < ranges:
            cell = self.m_grid21.GetCellValue(i,0)
            if cell == '':
                row = i
                i = ranges
            if i == (ranges-1):
                self.m_grid21.AppendRows(1, True)
                ranges = self.m_grid21.GetNumberRows()
            i = i +1
        self.m_grid21.SetCellValue(row,0,self.m_textCtrl50y.GetValue())
        self.m_grid21.SetCellValue(row,1,self.m_textCtrl50z.GetValue())        
        self.m_grid21.SetCellValue(row,2,self.m_textCtrl50a.GetValue())        
        self.m_grid21.SetCellValue(row,3,self.m_textCtrl50b.GetValue())        
        self.m_grid21.SetCellValue(row,4,self.m_textCtrl50c.GetValue())        
        self.m_grid21.SetCellValue(row,5,self.m_textCtrl50d.GetValue())        
        self.m_grid21.SetCellValue(row,6,self.m_textCtrl50e.GetValue())    
        
    def OnClearRange(self, event):

        """Remove the last range from the Calibration Ranges table"""

        ranges = self.m_grid21.GetNumberRows()
        i = 0
        while i < ranges:
            cell = self.m_grid21.GetCellValue(i,0)
            if cell == '':
                row = i-1
                i = ranges
            if i == (ranges-1):
                row = i
            i = i +1
        
        if row>-1:
            for i in range(0,7):
                self.m_grid21.SetCellValue(row,i,'')    
                
    def ProgressUpdate(self,Label,Status,colour):

        """
        Update the status tracker in the Run tab. Parameters are Label of the heading to update, 
        the string to update to and the colour of the text as a wx.colour 
        """        

        if Status == 'Error':
            obj = self.LastObj
            colour = wx.Colour(255,0,0)            
            
        if Label == "Creating Instruments:":
            obj = self.m_staticText123b
            self.m_staticText124b.SetValue(' ')
            self.m_staticText125b.SetValue(' ')
            
        elif Label == "Safety Checks:":
            obj = self.m_staticText124b
            self.m_staticText125b.SetValue(' ')
        elif Label == "Data Collection:":
            obj = self.m_staticText125b
            
        #obj.SetDefaultStyle(wx.TextAttr(wx.NullColour, colour))
        obj.SetForegroundColour(colour)
        obj.SetValue(Status)
        self.LastObj = obj 
    
    def OnGenerateTable(self,event):

        """
        If a table has been loaded, calls CreateInstrumets and then GenerateTable.
        """

        #check that the ranges are inputed correctly?
        if self.loaded_dict == True:
            instruments = self.CreateInstruments()
            self.GenerateTable(instruments)
        else: print("Load instrument dictionaries")
    
    def GenerateTable(self,instruments):

        """
        Generate table according to the calibration ranges table. The ranges 
        entered into the table are drawn from the insruments given as parameters
        """

        grid = self.m_grid3 #The grid to be used.
        #Make the grid 0 by 0, so it enlarges to exactly the right size when data is inputted. 
        if grid.GetNumberRows()>0:
            grid.DeleteRows(0,grid.GetNumberRows() ,True)
        if grid.GetNumberCols()>0:
            grid.DeleteCols(0,grid.GetNumberCols() ,True)
        
        range_table = self.m_grid21 #Table containing the ranges for the calibration.
        cal_ranges = []
        for row in range(range_table.GetNumberRows()):
            info = [str(range_table.GetCellValue(row,i)) for i in range(7)]
            if all(info): #Checks if ALL elements of info are non-empty/non-zero.
                cal_ranges.append(info)
                
                
        ranges = []
        for inst in instruments:
            ranges.append(inst.range) #Collects the physical ranges of the instrument.
            #Recall that those could be different to the calibration ranges, eg:
            #Instrument can have a range (0,12) but we want to do a buildup on (0,10).
        rm,rs,rx = ranges #split up into range meter, range source, range sourceX.
        GridFactory = GridMaker.GridPrinter(self,grid)
        
        full_cols = GridFactory.ColMaker(rm,rs,rx,cal_ranges) #Thats it, grid is made. All the previous stuff was colelcting info.
        for col,i in zip(full_cols, range(1,10)):
            GridFactory.PrintCol(col,i,8)
            #This prints the column to the table, since GridFactory has acess to the table in the GUI.
            #This is because this instance of the class was sent to the grid maker.
        #Just a long list of headers:
        titles = ["X Range", "X Settings (V)","S Range","S Settings (V)","DVM Range","Nominal reading",\
                  "#Readings","Delay (S)","DVM pause","DVM status","S status","X status","Mean","STD"]
        GridFactory.PrintRow(titles,1,7)
        info = ["Start Row",8,"Stop Row",grid.GetNumberRows()]
        GridFactory.PrintRow(info,0,4)
        info = ["instruments:","Meter: "+str(self.meter.label),"S: "+str(self.sourceS.label),"X: "+str(self.sourceX.label)]
        GridFactory.PrintRow(info,0,3)

        self.filled_grid = True #Flag that the grid was sucessfully filled up.
        self.m_grid3.Layout()
        
    def OnAnalysisFile(self, event):

        """
        from MIEcalculator, graph_gui.py.
        """

        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a project file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)
        
        analysis_file = None
        
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            print(filename)
            dirname = dlg.GetDirectory()
            print(dirname)
            analysis_file = os.path.join(dirname, filename)
        dlg.Destroy()
        if analysis_file: self.Analysis_file_name.SetLabel(analysis_file)
        
    def OnAnalyse(self,event):

        """
        Reads the name of the file to analyse,
        and sends it to the analysis object analysis.Analyser
        """

        #read a text box to get the name of file to analyse
        #create analysis object, send it the name of the file
        #it updates the file, adding the ratios.
        #call fill grid to load the new file up and replace the old one.
        
        xcel_name = str(self.Analysis_file_name.GetValue())#'Book1.xlsx'
        print(xcel_name)
        xcel_sheet = 'Sheet'
        
        analyser = analysis.Analyser(xcel_name,xcel_sheet)
        analyser.analysis()
        analyser.Save(xcel_name)
        controlgrid = tables.TABLES(self)
        printed_results = controlgrid.excel_to_grid(xcel_name, 'Results', self.m_grid4)
        printed_results_ratios = controlgrid.excel_to_grid(xcel_name, 'Gain Ratios', self.m_grid4b)
            
        
        #Perhaps find a good place to put back to the table.
        
    def OnSaveTables(self,event):

        """
        from MIEcalculator, graph_gui.py.
        """

        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        wildcard = "Poject source (*.csv; *.xls; *.xlsx; *.xlsm)|*.csv;*.xls; *.xlsx; *.xlsm|" \
         "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, "Choose a project file", self.dirname, "",
        wildcard, wx.OPEN | wx.MULTIPLE)
        
        save_file = None
        
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            save_file = os.path.join(dirname, filename)
        dlg.Destroy()
        if save_file: self.SaveGrid(save_file)

    def SaveGrid(self,path):

        """
        Saves using the tables.TABLES object
        """

        controlgrid = tables.TABLES(self)
        controlgrid.grid_to_excel(path, [(self.m_grid3,"Control"),(self.m_grid2,"Dict"),(self.m_grid21,"Ranges")])
        
    def on_grid_edited(self, event):

        """When one of the two input grids is edited, disable the run button."""

        self.filled_grid = False
        #This prevents the user from running the program until they press
        #the fill grid button, and update the grid.
        
    def DoReset(self, event):
  
        """
        Resets by clearing the data, and clearing the on screen text feedback.
        Also sets the Make Safe button back to green.
        """

        #reset the data, and clear the text box
        self.doStop()
        self.data.reset_list()
        self.m_textCtrl81.Clear()
        self.m_button12.SetBackgroundColour(wx.Colour(0, 255, 0))
        

    def OnStart(self, event):
        
        """
        Creates the instruments, and calls the doStart function. 
        """

        log = self.m_textCtrl81 # where stdout will be redirected
        redir = stuff.RedirectText(log)
        sys.stdout = redir #print statements, note to avoid 'print' if callafter delay is an issue
        sys.stderr = redir #python errors
        if self.filled_grid == True:
            if self.m_checkBox3.IsChecked():
                instruments = self.CreateInstruments()
                self.doStart(instruments)
            else:
                self.CheckCalibration()
        else:
            print("Input grids changed, generate a table again to continue")
            
    def CheckCalibration(self):

        """
        Generate and show confirmation window to check DC Zero Calibration.`
        """
        
        popup = Confirmation()
        popup.Show()
        
    def CreateInstruments(self):

        """
        Reads the dictionary uploaded to the grid, and creates gpib_inst.INSTRUMENT accordingly.
        Instruments must be the meter on the left, source S in the middle, source X on the right.
        """

        def sim(s):

            """Nested function used only here, returns a simplified string"""

            s = s.replace('\\r','\r')
            s = s.replace('\\n','\n')
            #Other simplifications might be necessary for additional instruments.
            return s
        
        dicts = self.m_grid2
        dm={} #Meter dictionary
        dx={} #X dictionary
        ds={} #S dictionary
        rows = dicts.GetNumberRows()
        for row in range(rows):
            dm.update({sim(dicts.GetCellValue(row, 0)):sim(dicts.GetCellValue(row, 1))})
            ds.update({sim(dicts.GetCellValue(row, 2)):sim(dicts.GetCellValue(row, 3))})
            dx.update({sim(dicts.GetCellValue(row, 4)):sim(dicts.GetCellValue(row, 5))})
        #Unpack the dictionaries to each respective instrument.
        self.meter = gpib_inst.INSTRUMENT(self.inst_bus, 'M', address=self.Meteraddress.GetValue(), **dm)
        self.sourceS = gpib_inst.INSTRUMENT(self.inst_bus, 'S', address=self.Saddress.GetValue(), **ds)
        self.sourceX = gpib_inst.INSTRUMENT(self.inst_bus, 'X', address=self.Xaddress.GetValue(), **dx)        
        return [self.meter, self.sourceS, self.sourceX]

    def OnOverideSafety(self,event):
        self.OverideSafety = True

    def OnCompleteChecks(self,event):
        self.OverideSafety = False
    
    def doStart(self,instruments):

        """
        Starts the algorithm, sends the created instruments to the wroker thread.
        """
        
        self.meter,self.sourceS,self.sourceX = instruments
        #first read essential setup info from the control grid (self.m_grid3).        
        grid = self.m_grid3
        grid.EnableEditing(False)
        #int(float()) is needed because the grid has loaded,e.g. 2.0 instead of 2
        start_row = int(float(grid.GetCellValue(3,1)))-1#wxgrid starts at zero
        stop_row = int(float(grid.GetCellValue(3,3)))-1
        sX_range_col = 1#source X range column
        sX_setting_col = 2#source X setting column
        sS_range_col = 3
        sS_setting_col = 4
        dvm_range_col = 5
        dvm_nominal_col = 6
        dvm_nordgs_col = 7
        delay_col = 8

        self.START_TIME = time.localtime()
        
        #DISABLE BUTTONS
        for button in [self.m_menuItem21,self.m_menuItem11,self.m_menuItem111,\
                       self.m_menuItem2,self.m_menuItem1,self.m_menuItem25,\
                       self.m_menuItem26,self.m_button15,self.m_button16]:
            button.Enable(False)
        
        #now call the thread
        if not self.worker1:
            self.worker1 = gpib_data.GPIBThreadF(self, self.EVT_RESULT_ID_1,\
            [self.inst_bus, grid, start_row, stop_row, dvm_nordgs_col, self.meter,\
             dvm_range_col, self.sourceX, sX_range_col, sX_setting_col,self.sourceS,\
             sS_range_col, sS_setting_col,delay_col, self.Analysis_file_name],\
            self.data,self.START_TIME,self.OverideSafety,self)
            #It has a huge list of useful things that it needs.
            
    def OnStop(self, event):
        self.doStop()
        
    def doStop(self):

        """
        Flags the worker thread to stop running if it exists.
        """

        # Flag the worker thread to stop if running
        if self.worker1:
            print('Halting GPIB data gathering')
            self.worker1.abort() 
            
    def OnMakeSafe(self, event):

        """
        Flags all threads to stop.
        """

        if self.worker1:
            self.worker1.MakeSafe()
        self.doStop() #stop main data gathering
        self.paused = True 
        #self.m_button2.SetLabel("Plot")

        # next run a gpib thread that sets sources to zero and standby and meter to autorange HV?
        
    def OnResult1(self, event):

        """Show Result status, event for termination of gpib thread"""
        
        #ENABLE BUTTONS
        for button in [self.m_menuItem21,self.m_menuItem11,self.m_menuItem111,\
                       self.m_menuItem2,self.m_menuItem1,self.m_menuItem25,\
                       self.m_menuItem26,self.m_button15,self.m_button16]:
            button.Enable(True)

        if event.data is None:
            # Thread aborted (using our convention of None return)
            print('GPIB data aborted'), time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        else:
            # Process results here
            print 'GPIB Result: %s'%event.data, time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            if event.data == "UNSAFE":
                self.m_button12.SetBackgroundColour(wx.Colour(255, 0, 0))
        
        
        # In either event, the worker is done
        self.worker1 = None
        self.m_grid3.EnableEditing(True)


    def OnGetInstruments(self, event):
        rm = self.inst_bus.ResourceManager()#new Visa
        try:
            #check = self.inst_bus.get_instruments_list()
            check = rm.list_resources()#new Visa
        except self.inst_bus.VisaIOError:
            check = "visa error"
        self.m_textCtrl8.SetValue(repr(check))
        self.m_panel7.SendSizeEvent()#forces textCtrl8 to resize to content

    def OnRefreshInstruments(self, event):

        """
        Adds all active instrument addresses to the drop down selection for the instruments.
        """

        rm = self.inst_bus.ResourceManager()#new Visa
        try:
            resources = rm.list_resources()
            self.Meteraddress.Clear()
            self.Saddress.Clear()
            self.Xaddress.Clear()
            for address in resources:
                self.Meteraddress.Append(address)
                self.Saddress.Append(address)
                self.Xaddress.Append(address)
                
        except self.inst_bus.VisaIOError:
            resources = "visa error"
        #self.m_textCtrl8.SetValue(repr(check))

        
    def OnInterfaceClear(self, event):
        rm = self.inst_bus.ResourceManager()#new Visa
        #self.inst_bus.Gpib().send_ifc()
        bus = rm.open_resource('GPIB::INTFC')#opens the GPIB interface
        bus.send_ifc()
        
    def OnSendTestCommand(self, event):

        """
        Sends a test command to the selected instrument using doSend.
        """

        name = self.m_comboBox8.GetValue()
        if name == 'Meter':
            address = self.Meteraddress.GetValue()
            self.doOnSend(address)
        elif name == 'Reference source (S)' :
            address = self.Saddress.GetValue()
            self.doOnSend(address)
        elif name == 'To calibrate (X)':
            address = self.Xaddress.GetValue()
            self.doOnSend(address)
        else:
            self.m_textCtrl23.AppendText('select instrument\n')

    def doOnSend(self,address):

        """ sends the commend to the address specified,
        creates a new visa resource manager."""

        try:
            command = self.m_textCtrl18.GetValue()
            rm = self.inst_bus.ResourceManager()#new Visa
            instrument = rm.open_resource(address)
            instrument.write(command)
            self.m_textCtrl23.AppendText(command+'\n')
        except self.inst_bus.VisaIOError:
            self.m_textCtrl23.AppendText('Failed to send\n')
            
        
    def OnReadTestCommand(self, event):

        """
        Reads from whatever instrument is selected using doRead.
        Will fail if it finds nothing on the instrument bus.
        """

        instrument = self.m_comboBox8.GetValue()
        if instrument == 'Meter':
            address = self.Meteraddress.GetValue()
            self.doRead(address)
        elif instrument == 'Reference source (S)' :
            address = self.Saddress.GetValue()
            self.doRead(address)
        elif instrument == 'To calibrate (X)':
            address = self.Xaddress.GetValue()
            self.doRead(address)
        else:
            self.m_textCtrl23.AppendText('select instrument\n')
        
    def doRead(self,address):

        """reads from the specified address"""

        rm = self.inst_bus.ResourceManager()#new Visa
        instrument = rm.open_resource(address)
        try:
            value = instrument.read_raw()
            self.m_textCtrl23.AppendText(repr(value)+'\n')
            return
        except self.inst_bus.VisaIOError:
            self.m_textCtrl23.WriteText('Failed to read\n')
            return

    def OnHelp(self,event):
        dlg = HelpBox(None)
        html = dlg.m_htmlWin1
        name = 'Manual.html'
        html.LoadPage(name)
        dlg.Show()
        
    def OnVal(self,event):
        if self.Validate == False:
            self.Validate = True
            
    def OnNoVal(self, event):
        if self.Validate == True:
            self.Validate = False

        
        
    def OnAbout(self,event):
        info = wx.AboutDialogInfo()
        info = wx.AboutDialogInfo()
        info.SetName('Ref step')
        info.SetVersion('2.0.0')
        info.SetDescription("description")
        info.SetCopyright('(C) 2017-2018 Measurement Standards Laboratory of New Zealand')
        info.SetWebSite('http://www.measurement.govt.nz/')
        info.SetLicence("Use it well")
        info.AddDeveloper('some code monkey(s)')
        wx.AboutBox(info)

    
    def OnClose(self, event):

        """
        Make sure threads not running if frame is closed before stopping everything.
        Seems to generate errors, but at least the threads do get stopped!
        The delay after stopping the threads need to be longer than the time for
        a thread to normally complete? Since thread needs to be able to
        post event back to the main frame.
        """

        if self.worker1: #stop main GPIB thread
            self.worker1.abort()
            time.sleep(0.3)
        self.Destroy()

class HelpBox (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(500,300), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_htmlWin1 = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(1500,1250), wx.html.HW_SCROLLBAR_AUTO)
        gbSizer4.Add(self.m_htmlWin1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)


        self.SetSizer(gbSizer4)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class Confirmation (wx.Frame):
    
    """ 
    Creates window to remind user to perform a DC Zero calibration on the instruments.
    User can either confirm that instruments are calibrated or can decide it is not 
    neccesary for the next run of tests.
    """
    
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Sources not calibrated?',size=(800,130))
        panel=wx.Panel(self, -1)
        
        msg = "Instruments need to undergo DC Zero Calibration. If already calibrated, ensure 'Instruments are Zero Calibrated' checkbox is filled."
        instructions = wx.StaticText(panel, label=msg)
        
        closeBtn = wx.Button(panel, label="Instruments have been DC zero calibrated")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        closeBtn2= wx.Button(panel, label="DC zero calibration is not required")
        closeBtn2.Bind(wx.EVT_BUTTON, self.onClose)
        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL|wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        sizer.Add(closeBtn2, 0, flags, 5)
        
        panel.SetSizer(sizer)
        
    def onClose(self, event):
        self.Close()



if __name__ == "__main__":
    app = wx.App()
    GraphFrame(None)
    app.MainLoop()
