# -*- coding: utf-8 -*-
from odoo import _, http
from odoo.http import request, route
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class GadrEventPage(CustomerPortal):
    
    def _events_get_page_view_values(self, event, access_token, **kwargs):
        values = {
            'page_name': 'events_page',
            'event_record': event,
        }
        return self._get_page_view_values(event, access_token, values, 'gadr_event_history', False, **kwargs)
     
    @http.route(['/events', '/events/page/<int:page>'], type='http', auth="public", website=True)
    def portal_events(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        GadrEvent = request.env['gadr.projects.event']
        domain =[("type", "=", 'event')]
                #searchbar sortings
        # count for pager
        events_count = GadrEvent.search_count(domain)
        # pager
        pager = portal_pager(
            url="/events",
            total=events_count,
            page=page,
            step=4
        )
        # content according to pager and archive selected
        gadr_event = GadrEvent.search(domain, order='create_date desc', limit=4, offset=pager['offset'])
        request.session['gadr_event_history'] = gadr_event.ids[:100]
        
        values.update({
            'gadr_event': gadr_event,
            'page_name': 'events_page',
            'pager': pager,
            'default_url': '/events',
        })
        return request.render("gadr_website.portal_events_page", values)
    
    @http.route(['/event/<int:event_id>'], type='http', auth="public", website=True)
    def portal_event_detail(self, event_id, access_token=None, **kw):
        GadrEvent = request.env['gadr.projects.event']
        domain =[("type", "=", 'event')]
        try:
            gadr_event_sudo = self._document_check_access('gadr.projects.event', event_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/')

       
        values = self._events_get_page_view_values(gadr_event_sudo, access_token, **kw)
        values.update({
            'last_gadr_event': GadrEvent.search(domain, order='create_date desc', limit=3)
        })
        return request.render("gadr_website.event_template", values)