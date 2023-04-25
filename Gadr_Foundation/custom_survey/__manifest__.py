# -*- coding: utf-8 -*-
{
    'name': "Custom Survey",
    'category': 'Marketing/Surveys',

    'summary': """""",

    'description': """
    """,

    'author': "",
    'website': "",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['survey','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/survey_survey_views.xml',
        'views/survey_templates.xml',
        'wizard/survey_user_input_report_xlsx_view.xml',
        'views/survey_report.xml',
        'report/report_action.xml'
    ],
}
