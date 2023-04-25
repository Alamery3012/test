# -*- coding: utf-8 -*-
from odoo import _, http
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class ProjectsPage(CustomerPortal):
    
    def _prepare_home_portal_values(self, counters):
        values = super(ProjectsPage, self)._prepare_home_portal_values(counters)
        if 'projects_count' in counters:
            projects_count = request.env['gadr.projects.event'].sudo().search_count(
                    [("type", "=", 'projects')],
                    order="create_date desc"
                )
            values['projects_count'] = projects_count
        return values
     
    @http.route(['/projects', '/projects/page/<int:page>'], type='http', auth="public", website=True)
    def portal_projects(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        GadrProjects = request.env['gadr.projects.event']
        domain =[("type", "=", 'projects')]
                #searchbar sortings
        # count for pager
        projects_count = GadrProjects.search_count(domain)
        # pager
        pager = portal_pager(
            url="/projects",
            total=projects_count,
            page=page,
            step=4
        )
        # content according to pager and archive selected
        gadr_projects = GadrProjects.search(domain, order='create_date desc', limit=4, offset=pager['offset'])
        request.session['gadr_projects_history'] = gadr_projects.ids[:100]
        
        values.update({
            'gadr_projects': gadr_projects,
            'page_name': 'projects_page',
            'pager': pager,
            'default_url': '/projects',
        })
        return request.render("gadr_website.portal_my_consultation_requests", values)
    
    @http.route(['/projects/event/<int:gadr_id>', '/projects/event/<int:gadr_id>/page/<int:page>'], type='http', auth="public", website=True)
    def portal_projects_event(self,gadr_id ,page=1, **kw):
        values = self._prepare_portal_layout_values()
        GadrProject = request.env['gadr.projects.event']
        domain =[("sector_ids", "=", gadr_id)]
                #searchbar sortings
        # count for pager
        projects_count = GadrProject.search_count(domain)
        # pager
        pager = portal_pager(
            url=f"/projects/event/{gadr_id}",
            total=projects_count,
            page=page,
            step=4
        )
        # content according to pager and archive selected
        gadr_projects_event = GadrProject.search(domain, order='create_date desc', limit=4, offset=pager['offset'])
        request.session['gadr_projects_event_history'] = gadr_projects_event.ids[:100]
        
        values.update({
            'gadr_projects_event': gadr_projects_event,
            
            'pager': pager,
            'default_url': f"/projects/event/{gadr_id}",
        })
        return request.render("gadr_website.portal_gadr_projects_event_requests", values)