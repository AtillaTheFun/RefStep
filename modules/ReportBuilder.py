# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:41:54 2018

@author: h.gibb
"""
import docx


class CalReport():
    def init(self, parent):
        self.name = parent.m_textCtrl188.GetValue()
        self.serial = parent.m_textCtrl189.GetValue()
        self.date = parent.m_textCtrl190.GetValue()
        self.client = parent.m_textCtrl191.GetValue()
        self.cond = parent.m_textCtrl191.GetValue()
        self.method =  parent.m_textCtrl192.GetValue()
        
        
    def BuildReport(self):
        doc = docx.Document()
        doc.add_heading('Calibration Report of a ' + self.name, 2)
        doc.add_paragraph('Serial: ' + self.serial)
        doc.add_paragraph('Date: '+self.date)
        doc.add_paragraph('Client: '+self.client)
        doc.add_paragraph('Calibration Conditions: ' +self.cond)
        doc.add_paragraph('Method: '+self.method)
        table = doc.add_table(rows=5, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Instrument Range'
        hdr_cells[1].text = 'Instrument Readout'
        hdr_cells[2].text = 'Expanded Uncertainty'
        

                
        doc.save('Calibration Report for '+self.name+'.docx')
