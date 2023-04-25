
# -*- coding: utf-8 -*-

from odoo.http import route, request, Controller
from odoo.exceptions import UserError, ValidationError


class VisitorPartner(Controller):
   
    @route('/visitor_partner', type='http', auth="public", website=True, csrf=False)
    def visitor_partner(self, **post):
        
        request.env["res.partner"].sudo().create({
            'is_visitor': True,
            'name':post.get("name"),
            'phone':post.get("phone") or '',
            'city':post.get("city") or '',
            'email':post.get("email"),
        })
        

        return request.render('gadr_website.visitor_thanks')
