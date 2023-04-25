# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta, time
from odoo import models, _


class SurveyUserInput(models.AbstractModel):
    _name = 'report.custom_survey.report_survey_user_input_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Survey User Input'

    def generate_xlsx_report(self, workbook, data, partners):
        title = workbook.add_format(
            {'bold': True, 'align': 'left', 'bg_color': '#acacac', 'font_color': '#000000',
             'border': False, 'font_size': 12})
        report_format_1 = workbook.add_format(
            {'font_size': 14, 'border': 1, 'align': 'center', 'bold': True, 'valign': 'vcenter', })
        report_format_2 = workbook.add_format({'font_size': 10, 'border': 1, 'align': 'center', 'valign': 'vcenter', })
        sheet = workbook.add_worksheet(_('Last purchase price xlsx report'))
        sheet.add_table('B3:AB21', {'header_row': False, 'autofilter': False,
                                    'style': 'Table Style Light 9'})
        
        col = 2
        row = 0
        for survey_id in data.get('data'):
            sheet.merge_range('C%s:J%s' % (col , col), '# %s' %  survey_id.get('survey_name'), title)
            for line in survey_id.get('lable'):
                sheet.write(col, row + 2, line.get('title'), report_format_1)
                sheet.set_column(col, row + 2, 30)
                row+= 1
            col+= 1
            con = 1
            roww = 2
            for lines in survey_id.get('display_names'):
                sheet.write(col, roww, lines.get('display_name'), report_format_2)
                roww+=1
                if con == int(survey_id.get('len_user_input_line')):
                    col += 1
                    con = 1
                    roww = 2 
                    continue
                con+= 1
            row = 0
            col+= 2