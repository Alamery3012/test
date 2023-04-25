# -*- coding: utf-8 -*-
{
    'name': 'Gadr Website Theme',
    'category': 'Website/Website',
    'version': '1.0',
    'Website': '',
    'depends': ['website','gadr_backend','survey'],

    # always loaded
    'data': [
        # 'templates/custom_website_templates.xml',
        # 'templates/homepage_template.xml',
        'views/index.xml',
        'views/homepage.xml',
        'views/projects_page.xml',
        'views/events_page.xml',
        'views/photo_albums_page.xml',
        'views/video_albums_page.xml',
        'views/aboutus_page.xml',
        'views/contact.xml',
        'views/gadr_sector_page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'gadr_website/static/src/css/all.css',
            # 'gadr_website/static/src/css/ff.css',
            'gadr_website/static/src/css/step_form_style.css',
            'gadr_website/static/src/css/swiper.css',
            'gadr_website/static/src/css/swiper-bundle.min.css',
            'gadr_website/static/src/css/style_swiper.css',
            # 'gadr_website/static/src/scss/style_projet.scss',
            'gadr_website/static/src/css/style_header.css',
            'gadr_website/static/src/css/style_footer.css',
            'gadr_website/static/src/css/style_social_madi.css',
            'gadr_website/static/src/css/aboutus_style.css',
            'gadr_website/static/src/css/style_contact_us.css',
            'gadr_website/static/src/css/style_home.css',
            'gadr_website/static/src/scss/color.scss',
            'gadr_website/static/src/scss/home/about_us_section.scss',
            'gadr_website/static/src/scss/home/activities_section.scss',
            
            #File Js
            'gadr_website/static/src/js/menu.js',
            'gadr_website/static/src/js/wsp.js',
            'gadr_website/static/src/js/slick.js',
            'gadr_website/static/src/js/swiper-bundle.min.js',
            'gadr_website/static/src/js/main.js',
            'gadr_website/static/src/js/change_mode.js',
            'gadr_website/static/src/js/visitor_thanks_page.js',
           
    ],
    },
    
    'application': True,
}
