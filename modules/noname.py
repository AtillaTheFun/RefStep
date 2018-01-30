# -*- coding: utf-8 -*-
##########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
#
# PLEASE DO "NOT" EDIT THIS FILE!
##########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid
import time
##########################################################################
# Class MyFrame1
##########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = u"Instrument Controller", pos = wx.DefaultPosition, size = wx.Size(1325,700), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
        
        self.m_auinotebook4 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.Point(-1,-1), wx.Size(-1,-1), 0)
        self.m_mgr.AddPane(self.m_auinotebook4, wx.aui.AuiPaneInfo() .Left() .CloseButton(False).MaximizeButton(True).MinimizeButton(True).PinButton(True).Dock().Resizable().FloatingSize(wx.DefaultSize) .MinSize(wx.Size(600,300)))
        
        self.m_panel511 = wx.Panel(self.m_auinotebook4, wx.ID_ANY, wx.Point(-1,-1), wx.Size(-1,-1), wx.TAB_TRAVERSAL)
        gbSizer311 = wx.GridBagSizer(0, 0)
        gbSizer311.SetFlexibleDirection(wx.BOTH)
        gbSizer311.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        MeteraddressChoices = []
        self.Meteraddress = wx.ComboBox(self.m_panel511, wx.ID_ANY, u"GPIB0::23::INSTR", wx.DefaultPosition, wx.DefaultSize, MeteraddressChoices, 0)
        gbSizer311.Add(self.Meteraddress, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        SaddressChoices = []
        self.Saddress = wx.ComboBox(self.m_panel511, wx.ID_ANY, u"GPIB0::15::INSTR", wx.DefaultPosition, wx.DefaultSize, SaddressChoices, 0)
        gbSizer311.Add(self.Saddress, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        XaddressChoices = []
        self.Xaddress = wx.ComboBox(self.m_panel511, wx.ID_ANY, u"GPIB0::4::INSTR", wx.DefaultPosition, wx.DefaultSize, XaddressChoices, 0)
        gbSizer311.Add(self.Xaddress, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText12 = wx.StaticText(self.m_panel511, wx.ID_ANY, u"Meter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gbSizer311.Add(self.m_staticText12, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button14 = wx.Button(self.m_panel511, wx.ID_ANY, u"Refresh instruments", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer311.Add(self.m_button14, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText13 = wx.StaticText(self.m_panel511, wx.ID_ANY, u"Reference source", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        gbSizer311.Add(self.m_staticText13, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText14 = wx.StaticText(self.m_panel511, wx.ID_ANY, u"To calibrate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        gbSizer311.Add(self.m_staticText14, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText121 = wx.StaticText(self.m_panel511, wx.ID_ANY, u"Test instruments:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText121.Wrap(-1)
        gbSizer311.Add(self.m_staticText121, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        m_comboBox8Choices = [ u"Meter", u"Reference source (S)", u"To calibrate (X)" ]
        self.m_comboBox8 = wx.ComboBox(self.m_panel511, wx.ID_ANY, u"Meter", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, 0)
        self.m_comboBox8.SetSelection(0)
        gbSizer311.Add(self.m_comboBox8, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_textCtrl18 = wx.TextCtrl(self.m_panel511, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer311.Add(self.m_textCtrl18, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_textCtrl23 = wx.TextCtrl(self.m_panel511, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250,100), wx.TE_MULTILINE)
        gbSizer311.Add(self.m_textCtrl23, wx.GBPosition(6, 0), wx.GBSpan(6, 2), wx.ALL, 5)
        
        self.m_button15 = wx.Button(self.m_panel511, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer311.Add(self.m_button15, wx.GBPosition(5, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button16 = wx.Button(self.m_panel511, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer311.Add(self.m_button16, wx.GBPosition(5, 3), wx.GBSpan(1, 1), wx.ALL, 5)
        
        
        self.m_panel511.SetSizer(gbSizer311)
        self.m_panel511.Layout()
        gbSizer311.Fit(self.m_panel511)
        self.m_auinotebook4.AddPage(self.m_panel511, u"Instruments", True, wx.NullBitmap)
        self.m_panel5 = wx.Panel(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), wx.TAB_TRAVERSAL)
        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_button13 = wx.Button(self.m_panel5, wx.ID_ANY, u"Generate a table", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_button13, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button11 = wx.Button(self.m_panel5, wx.ID_ANY, u"Open dictionary", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_button11, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        
        self.m_panel5.SetSizer(gbSizer3)
        self.m_panel5.Layout()
        gbSizer3.Fit(self.m_panel5)
        self.m_auinotebook4.AddPage(self.m_panel5, u"Control", False, wx.NullBitmap)
        self.m_panel4 = wx.Panel(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_button5 = wx.Button(self.m_panel4, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.m_button5, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button12 = wx.Button(self.m_panel4, wx.ID_ANY, u"Make Safe", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button12.SetBackgroundColour(wx.Colour(0, 255, 0))
        
        gbSizer6.Add(self.m_button12, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText51 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Event reports", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        gbSizer6.Add(self.m_staticText51, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_textCtrl81 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500,250), wx.TE_MULTILINE)
        gbSizer6.Add(self.m_textCtrl81, wx.GBPosition(3, 0), wx.GBSpan(1, 3), wx.ALL, 5)
        
        self.m_button6 = wx.Button(self.m_panel4, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.m_button6, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        
        self.m_panel4.SetSizer(gbSizer6)
        self.m_panel4.Layout()
        gbSizer6.Fit(self.m_panel4)
        self.m_auinotebook4.AddPage(self.m_panel4, u"Run", False, wx.NullBitmap)
        self.m_scrolledWindow5 = wx.ScrolledWindow(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow5.SetScrollRate(5, 5)
        gbSizer7 = wx.GridBagSizer(0, 0)
        gbSizer7.SetFlexibleDirection(wx.BOTH)
        gbSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.m_staticText10 = wx.StaticText(self.m_scrolledWindow5, wx.ID_ANY, u"Analysis file name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        gbSizer7.Add(self.m_staticText10, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.Analysis_file_name = wx.TextCtrl(self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.Analysis_file_name, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button122 = wx.Button(self.m_scrolledWindow5, wx.ID_ANY, u"Analyse data", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_button122, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_grid4 = wx.grid.Grid(self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid4.CreateGrid(5, 6)
        self.m_grid4.EnableEditing(True)
        self.m_grid4.EnableGridLines(True)
        self.m_grid4.EnableDragGridSize(False)
        self.m_grid4.SetMargins(0, 0)
        
        # Columns
        self.m_grid4.EnableDragColMove(False)
        self.m_grid4.EnableDragColSize(True)
        self.m_grid4.SetColLabelSize(30)
        self.m_grid4.SetColLabelValue(0, u"Name")
        self.m_grid4.SetColLabelValue(1, u"Ratio")
        self.m_grid4.SetColLabelValue(2, u"Uncert")
        self.m_grid4.SetColLabelValue(3, u"Dof")
        self.m_grid4.SetColLabelValue(4, u"Range")
        self.m_grid4.SetColLabelValue(5, u"V Setting Max/Min")
        
        
        self.m_grid4.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid4.EnableDragRowSize(True)
        self.m_grid4.SetRowLabelSize(80)
        self.m_grid4.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer7.Add(self.m_grid4, wx.GBPosition(1, 0), wx.GBSpan(1, 4), wx.ALL, 5)
        
        
        self.m_scrolledWindow5.SetSizer(gbSizer7)
        self.m_scrolledWindow5.Layout()
        gbSizer7.Fit(self.m_scrolledWindow5)
        self.m_auinotebook4.AddPage(self.m_scrolledWindow5, u"Analysis", False, wx.NullBitmap)
        
        
        
        # DC Offset Measurement ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        self.m_scrolledWindow49 = wx.Panel(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)


        gbSizer9 = wx.GridBagSizer(0, 0)

        
        self.m_scrolledWindow49 = wx.ScrolledWindow(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow49.SetScrollRate(10, 10)

        self.m_scrolledWindow49.SetSizer(gbSizer9)

        self.m_scrolledWindow49.Layout()
        gbSizer9.Fit(self.m_scrolledWindow49)  
        self.m_auinotebook4.AddPage(self.m_scrolledWindow49, u"DC Offset Measurement", False, wx.NullBitmap)

        self.m_button197 = wx.Button(self.m_scrolledWindow49, wx.ID_ANY, u"Begin Measurement", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer9.Add(self.m_button197, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        
        
        
# CALIBRATION REPORT ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.m_scrolledWindow48 = wx.Panel(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)


        gbSizer8 = wx.GridBagSizer(0, 0)

        
        self.m_scrolledWindow48 = wx.ScrolledWindow(self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow48.SetScrollRate(10, 10)

        self.m_scrolledWindow48.SetSizer(gbSizer8)

        self.m_scrolledWindow48.Layout()
        gbSizer8.Fit(self.m_scrolledWindow48)  
        self.m_auinotebook4.AddPage(self.m_scrolledWindow48, u"Calibration Report", False, wx.NullBitmap)
        
        self.m_checkBox1 = wx.CheckBox(self.m_scrolledWindow48, wx.ID_ANY, u"Calibrate Meter", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_checkBox1, wx.GBPosition(0,1), wx.GBSpan(1,1), wx.ALL, 5)
        self.m_checkBox1.SetValue(True)
        
        self.m_checkBox2 = wx.CheckBox(self.m_scrolledWindow48, wx.ID_ANY, u"Calibrate Source", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_checkBox2, wx.GBPosition(0,2), wx.GBSpan(1,1), wx.ALL, 5)
        
        self.m_button187 = wx.Button(self.m_scrolledWindow48, wx.ID_ANY, u"Choose Data", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_button187, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_textCtrl187 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, u"[DataFile.xlsx]", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        gbSizer8.Add(self.m_textCtrl187, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText188 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Instrument Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText188, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl188 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, u"[Instrument Name]", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_textCtrl188, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)
  
        self.m_staticText189 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Serial Number:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText189, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_textCtrl189 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, u"[Serial Number]", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_textCtrl189, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_staticText190 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText190, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        time_bit = time.strftime("%Y.%m.%d",time.localtime())
        self.m_textCtrl190 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, time_bit, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_textCtrl190, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        

        
        self.m_staticText191 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Client:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText191, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_textCtrl191 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, u"Client Name", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_textCtrl191, wx.GBPosition(5, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText196 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Calibration Conditions:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText196, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_textCtrl196 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,100), 0)
        gbSizer8.Add(self.m_textCtrl196, wx.GBPosition(6, 2), wx.GBSpan(1, 1), wx.ALL, 5)
 
  
        self.m_staticText192 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Description of Method:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText192, wx.GBPosition(7, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_textCtrl192 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,100), 0)
        gbSizer8.Add(self.m_textCtrl192, wx.GBPosition(7, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        
        self.m_textCtrl185 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,50), 0)
        gbSizer8.Add(self.m_textCtrl185, wx.GBPosition(8, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_staticText185 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Results:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText185, wx.GBPosition(8, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        
        
        
        self.m_grid41 = wx.grid.Grid(self.m_scrolledWindow48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        
        
        # Grid
        self.m_grid41.CreateGrid(5, 3)
        self.m_grid41.EnableEditing(True)
        self.m_grid41.EnableGridLines(True)
        self.m_grid41.EnableDragGridSize(False)
        self.m_grid41.SetMargins(0, 0)
        
        # Columns
        self.m_grid41.EnableDragColMove(False)
        self.m_grid41.EnableDragColSize(True)
        self.m_grid41.SetColLabelSize(30)
        self.m_grid41.SetColLabelValue(0, u"Range")
        self.m_grid41.SetColLabelValue(1, u" Readout")
        self.m_grid41.SetColLabelValue(2, u"Uncert")
        self.m_grid41.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid41.EnableDragRowSize(True)
        self.m_grid41.SetRowLabelSize(20)
        self.m_grid41.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid41.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer8.Add(self.m_grid41, wx.GBPosition(9, 2), wx.GBSpan(1, 4), wx.ALL, 5)
        
        self.m_staticText193 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"DC Volatge Offset:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText193, wx.GBPosition(9, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        
        self.m_grid42 = wx.grid.Grid(self.m_scrolledWindow48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid42.CreateGrid(5, 5)
        self.m_grid42.EnableEditing(True)
        self.m_grid42.EnableGridLines(True)
        self.m_grid42.EnableDragGridSize(False)
        self.m_grid42.SetMargins(0, 0)
        
        # Columns
        self.m_grid42.EnableDragColMove(False)
        self.m_grid42.EnableDragColSize(True)
        self.m_grid42.SetColLabelSize(30)
        self.m_grid42.SetColLabelValue(0, u"Range")
        self.m_grid42.SetColLabelValue(1, u" Readout")
        self.m_grid42.SetColLabelValue(2, u"Voltage +")
        self.m_grid42.SetColLabelValue(3, u"Voltage -")
        self.m_grid42.SetColLabelValue(4, u"Uncert")

        self.m_grid42.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid42.EnableDragRowSize(True)
        self.m_grid42.SetRowLabelSize(20)
        self.m_grid42.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid42.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer8.Add(self.m_grid42, wx.GBPosition(10, 2), wx.GBSpan(1, 4), wx.ALL, 5)
        
        self.m_staticText194 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"DC Volatge Gain:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText194, wx.GBPosition(10, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        
        self.m_grid43 = wx.grid.Grid(self.m_scrolledWindow48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid43.CreateGrid(5, 4)
        self.m_grid43.EnableEditing(True)
        self.m_grid43.EnableGridLines(True)
        self.m_grid43.EnableDragGridSize(False)
        self.m_grid43.SetMargins(0, 0)
        
        # Columns
        self.m_grid43.EnableDragColMove(False)
        self.m_grid43.EnableDragColSize(True)
        self.m_grid43.SetColLabelSize(30)
        self.m_grid43.SetColLabelValue(0, u"Readout")
        self.m_grid43.SetColLabelValue(1, u"Relative +")
        self.m_grid43.SetColLabelValue(2, u"Relative -")
        self.m_grid43.SetColLabelValue(3, u"Uncert")

        self.m_grid43.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid43.EnableDragRowSize(True)
        self.m_grid43.SetRowLabelSize(20)
        self.m_grid43.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid43.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer8.Add(self.m_grid43, wx.GBPosition(11, 2), wx.GBSpan(1, 4), wx.ALL, 5)

        self.m_staticText195 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"DC Volatge Linearity:", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText195, wx.GBPosition(11, 1), wx.GBSpan(1, 1), wx.ALL, 5)

  
        time_bit = time.strftime("%Y",time.localtime())
          
        self.m_staticText810 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Report No.", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText810, wx.GBPosition(12, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_textCtrl810 = wx.TextCtrl(self.m_scrolledWindow48, wx.ID_ANY, u"Electrical/"+time_bit+"/____/Day Month Year", wx.DefaultPosition, wx.Size(400,30), 0)
        gbSizer8.Add(self.m_textCtrl810, wx.GBPosition(12,2), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_button822 = wx.Button(self.m_scrolledWindow48, wx.ID_ANY, u"Create Report" , wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_button822, wx.GBPosition(13, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_grid44 = wx.grid.Grid(self.m_scrolledWindow48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid44.CreateGrid(5, 4)
        self.m_grid44.EnableEditing(True)
        self.m_grid44.EnableGridLines(True)
        self.m_grid44.EnableDragGridSize(False)
        self.m_grid44.SetMargins(0, 0)
        
        # Columns
        self.m_grid44.EnableDragColMove(False)
        self.m_grid44.EnableDragColSize(True)
        self.m_grid44.SetColLabelSize(30)
        self.m_grid44.SetColLabelValue(0, u"Label")
        self.m_grid44.SetColLabelValue(1, u"Ratio")
        self.m_grid44.SetColLabelValue(2, u"STDEV")
        self.m_grid44.SetColLabelValue(3, u"Effct. DoF")
        self.m_grid44.SetColLabelValue(3, u"Range")
        
        
        self.m_grid44.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid44.EnableDragRowSize(True)
        self.m_grid44.SetRowLabelSize(20)
        self.m_grid44.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid44.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer8.Add(self.m_grid44, wx.GBPosition(14, 2), wx.GBSpan(1, 4), wx.ALL, 5)
        self.m_staticText195 = wx.StaticText(self.m_scrolledWindow48, wx.ID_ANY, u"Ratio Data", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.m_staticText195, wx.GBPosition(14, 1), wx.GBSpan(1, 1), wx.ALL, 5)


  
  # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu11 = wx.Menu()
        self.m_menuItem21 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Open dictionary", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem21)
        
        self.m_menuItem11 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Save tables", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem11)
        
        self.m_menuItem111 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Analysis file", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem111)
        
        self.m_menuItem1111 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Reset", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem1111)
        
        self.m_menu1 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Live instruments", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu1.AppendItem(self.m_menuItem2)
        
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Simulated instruments", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu1.AppendItem(self.m_menuItem1)
        
        self.m_menu11.AppendSubMenu(self.m_menu1, u"Run Options")
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem26 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Complete checks", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu2.AppendItem(self.m_menuItem26)
        self.m_menuItem26.Check(True)
        
        self.m_menuItem25 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Overide safety", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu2.AppendItem(self.m_menuItem25)
        
        self.m_menu11.AppendSubMenu(self.m_menu2, u"Safety")
        
        self.m_menubar1.Append(self.m_menu11, u"File") 
        
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem46 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Regular Operation", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu3.AppendItem(self.m_menuItem46)
        self.m_menuItem46.Check(True)
        
        self.m_menuItem45 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Validation", wx.EmptyString, wx.ITEM_RADIO)
        self.m_menu3.AppendItem(self.m_menuItem45)
        

        self.m_menubar1.Append(self.m_menu3, u"Validation")         
        
        self.m_menu13 = wx.Menu()
        self.m_menuItem30 = wx.MenuItem(self.m_menu13, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu13.AppendItem(self.m_menuItem30)
        
        self.m_menuItem31 = wx.MenuItem(self.m_menu13, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu13.AppendItem(self.m_menuItem31)
        
        self.m_menubar1.Append(self.m_menu13, u"Help") 
       
        
        
        self.SetMenuBar(self.m_menubar1)
        
        self.m_auinotebook41 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.Point(-1,-1), wx.Size(500,-1), 0)
        self.m_auinotebook41.SetMinSize(wx.Size(200,300))
        
        self.m_mgr.AddPane(self.m_auinotebook41, wx.aui.AuiPaneInfo() .Right() .CloseButton(False).MaximizeButton(True).MinimizeButton(True).PinButton(True).Dock().Resizable().FloatingSize(wx.DefaultSize).MinSize(wx.Size(600,300)))
        
        self.m_scrolledWindow4 = wx.ScrolledWindow(self.m_auinotebook41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow4.SetScrollRate(5, 5)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid2 = wx.grid.Grid(self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid2.CreateGrid(13, 6)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)
        
        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer2.Add(self.m_grid2, 0, wx.ALL, 5)
        
        
        self.m_scrolledWindow4.SetSizer(bSizer2)
        self.m_scrolledWindow4.Layout()
        bSizer2.Fit(self.m_scrolledWindow4)
        self.m_auinotebook41.AddPage(self.m_scrolledWindow4, u"Instrument commands", True, wx.NullBitmap)
        self.m_scrolledWindow41 = wx.ScrolledWindow(self.m_auinotebook41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow41.SetScrollRate(5, 5)
        bSizer21 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid21 = wx.grid.Grid(self.m_scrolledWindow41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid21.CreateGrid(8, 7)
        self.m_grid21.EnableEditing(True)
        self.m_grid21.EnableGridLines(True)
        self.m_grid21.EnableDragGridSize(False)
        self.m_grid21.SetMargins(0, 0)
        
        # Columns
        self.m_grid21.SetColSize(0, 80)
        self.m_grid21.SetColSize(1, 80)
        self.m_grid21.SetColSize(2, 80)
        self.m_grid21.SetColSize(3, 132)
        self.m_grid21.SetColSize(4, 142)
        self.m_grid21.SetColSize(5, 80)
        self.m_grid21.SetColSize(6, 80)
        self.m_grid21.EnableDragColMove(False)
        self.m_grid21.EnableDragColSize(True)
        self.m_grid21.SetColLabelSize(30)
        self.m_grid21.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid21.EnableDragRowSize(True)
        self.m_grid21.SetRowLabelSize(80)
        self.m_grid21.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid21.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer21.Add(self.m_grid21, 0, wx.ALL, 5)
        
        self.m_button151 = wx.Button(self.m_scrolledWindow41, wx.ID_ANY, u"Add Row", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_button151, 0, wx.ALL, 5)
        
        
        self.m_scrolledWindow41.SetSizer(bSizer21)
        self.m_scrolledWindow41.Layout()
        bSizer21.Fit(self.m_scrolledWindow41)
        self.m_auinotebook41.AddPage(self.m_scrolledWindow41, u"Calibration ranges", False, wx.NullBitmap)
        self.m_scrolledWindow3 = wx.ScrolledWindow(self.m_auinotebook41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        self.m_scrolledWindow3.SetScrollRate(5, 5)
        self.m_scrolledWindow3.SetMinSize(wx.Size(200,300))
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_grid3 = wx.grid.Grid(self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        # Grid
        self.m_grid3.CreateGrid(5, 5)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)
        
        # Columns
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        # Label Appearance
        
        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.m_grid3, 0, wx.ALL, 5)
        
        
        self.m_scrolledWindow3.SetSizer(bSizer1)
        self.m_scrolledWindow3.Layout()
        bSizer1.Fit(self.m_scrolledWindow3)
        self.m_auinotebook41.AddPage(self.m_scrolledWindow3, u"Control settings", False, wx.NullBitmap)
        
        
        self.m_mgr.Update()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.m_button187.Bind(wx.EVT_BUTTON, self.OnOpenData)
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.OnMeter)
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, self.OnSource)
        self.m_button822.Bind(wx.EVT_BUTTON, self.OnCreateReport)
        self.m_button14.Bind(wx.EVT_BUTTON, self.OnRefreshInstruments)
        self.m_button15.Bind(wx.EVT_BUTTON, self.OnSendTestCommand)
        self.m_button16.Bind(wx.EVT_BUTTON, self.OnReadTestCommand)
        self.m_button13.Bind(wx.EVT_BUTTON, self.OnGenerateTable)
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnOpenDict)
        self.m_button5.Bind(wx.EVT_BUTTON, self.OnStart)
        self.m_button12.Bind(wx.EVT_BUTTON, self.OnMakeSafe)
        self.m_button6.Bind(wx.EVT_BUTTON, self.OnStop)
        self.m_button122.Bind(wx.EVT_BUTTON, self.OnAnalyse)
        #self.m_button2.Bind(wx.EVT_BUTTON, self.OnPauseButton)
        self.Bind(wx.EVT_MENU, self.OnOpenDict, id = self.m_menuItem21.GetId())
        self.Bind(wx.EVT_MENU, self.OnSaveTables, id = self.m_menuItem11.GetId())
        self.Bind(wx.EVT_MENU, self.OnAnalysisFile, id = self.m_menuItem111.GetId())
        self.Bind(wx.EVT_MENU, self.DoReset, id = self.m_menuItem1111.GetId())
        self.Bind(wx.EVT_MENU, self.OnLive, id = self.m_menuItem2.GetId())
        self.Bind(wx.EVT_MENU, self.OnSimulate, id = self.m_menuItem1.GetId())
        self.Bind(wx.EVT_MENU, self.OnCompleteChecks, id = self.m_menuItem26.GetId())
        self.Bind(wx.EVT_MENU, self.OnOverideSafety, id = self.m_menuItem25.GetId())
        self.Bind(wx.EVT_MENU, self.OnHelp, id = self.m_menuItem30.GetId())
        self.Bind(wx.EVT_MENU, self.OnAbout, id = self.m_menuItem31.GetId())
        self.Bind(wx.EVT_MENU, self.OnVal, id = self.m_menuItem45.GetId())
        self.Bind(wx.EVT_MENU, self.OnNoVal, id = self.m_menuItem46.GetId())
        self.m_grid21.Bind(wx.EVT_CHAR, self.on_grid_edited)
        self.m_button151.Bind(wx.EVT_BUTTON, self.OnAddRow)
    
    def __del__(self):
        self.m_mgr.UnInit()
        
    
    
    # Virtual event handlers, overide them in your derived class
    def OnOpenData(self,event):
        event.skip()
    
    def OnMeter(self, event):
        event.Skip()
        
    def OnSource(self, event):
        event.Skip()
    
    def OnClose(self, event):
        event.Skip()
    
    def OnRefreshInstruments(self, event):
        event.Skip()
    
    def OnSendTestCommand(self, event):
        event.Skip()
    
    def OnReadTestCommand(self, event):
        event.Skip()
    
    def OnGenerateTable(self, event):
        event.Skip()
    
    def OnOpenDict(self, event):
        event.Skip()
    
    def OnStart(self, event):
        event.Skip()
    
    def OnMakeSafe(self, event):
        event.Skip()
    
    def OnStop(self, event):
        event.Skip()
    
    def OnAnalyse(self, event):
        event.Skip()
    
    def OnPauseButton(self, event):
        event.Skip()
    
    
    def OnSaveTables(self, event):
        event.Skip()
    
    def OnAnalysisFile(self, event):
        event.Skip()
    
    def DoReset(self, event):
        event.Skip()
    
    def OnLive(self, event):
        event.Skip()
    
    def OnSimulate(self, event):
        event.Skip()
    
    def OnCompleteChecks(self, event):
        event.Skip()
    
    def OnOverideSafety(self, event):
        event.Skip()
    
    def OnHelp(self, event):
        event.Skip()
    
    def OnAbout(self, event):
        event.Skip()
        
    def OnVal(self, event):
        event.Skip()

    def OnNoVal(self, event):
        event.Skip()
    
    def on_grid_edited(self, event):
        event.Skip()
    
    def OnAddRow(self, event):
        event.Skip()
    

