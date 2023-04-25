from odoo import _, http
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal

class AboutUsPage(CustomerPortal):
    @route(["/aboutus",], type="http", auth="public", website=True)
    def aboutus(self, **kw):
        values = self._prepare_portal_layout_values()
        values.update({
            'page_name': 'aboutus_page',
            
        })
       
        return request.render("gadr_website.aboutus_page_template",values)