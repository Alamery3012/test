# -*- coding: utf-8 -*-
{
    'name': 'Gadr Backend',
    'category': 'Institution/Gadr',
    'version': '1.0',
    'Website': '',
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/gadr_sector_data.xml',
        'data/gadr_partner_data.xml',
        'views/carousel_slide_views.xml',
        'views/gadr_projects_event_views.xml',
        'views/gadr_media_media_views.xml',
        'views/visitor_partner_views.xml',
        'views/gadr_sector_views.xml',
        'views/gadr_partener_wiews.xml',
        'views/gadr_menu_views.xml',
        
    ],
    
    'installable': True,
    'application': True,
    # 'auto_install': True,
    'license': 'LGPL-3',
}
