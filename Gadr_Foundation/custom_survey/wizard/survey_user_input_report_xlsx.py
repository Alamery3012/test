# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.modules.module import get_module_resource

from odoo import models, fields, api, _



class SocialMediaNewsReport(models.TransientModel):
    _name = 'survey.user.input.report.xlsx'
    
    survey_ids = fields.Many2many('survey.survey')
    
    def print_action(self):
        survey_ids = self.env['survey.survey'].search([('id', 'in', self.survey_ids.ids)])
        data = []
        for survey_id in survey_ids:
            user_input_ids = self.env['survey.user_input'].search([('survey_id', '=', survey_id.id), ('state', '=', 'done')])
            data_dic = {}
            # print(i.question_and_page_ids.title)
            data_dic['survey_name'] =  survey_id.title
            data_dic['lable'] = [{'title': worked_days_id.title} 
                             for worked_days_id in survey_id.question_and_page_ids] if survey_id.question_and_page_ids else []
            user_input_line_list = []
            for user_input_id in user_input_ids:
                for worked_days_id in user_input_id.user_input_line_ids:
                    user_input_line_dict = {
                        'display_name': worked_days_id.display_name
                    }
                
                    user_input_line_list.append(user_input_line_dict)
                data_dic['len_user_input_line'] = len(user_input_id.user_input_line_ids)
            data_dic['display_names'] = user_input_line_list
            data.append(data_dic)  
        # print(data)
        action = self.env.ref('custom_survey.survey_user_input_excel_report').report_action(self, data={
            'data': data
        })
        action.update({'close_on_report_download': True})
        # print(data_list)
        return action