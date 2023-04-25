# -*- coding: utf-8 -*-

from odoo import _, http
from odoo.http import request, route
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager



class PhotoAlbums(CustomerPortal):
        
    @http.route(['/photo/albums', '/photo/albums/page/<int:page>'], type='http', auth="public", website=True)
    def portal_photo_albums(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        PhotoAlbums = request.env['gadr.media.media']
        domain =[('type', '=', 'photo_albums')]
                #searchbar sortings
        
        # count for pager
        photo_albums_count = PhotoAlbums.search_count(domain)
        # pager
        pager = portal_pager(
            url="/photo/albums",
            total=photo_albums_count,
            page=page,
            step=4
        )
        # content according to pager and archive selected
        photo_albums = PhotoAlbums.search(domain, order='create_date desc', limit=4, offset=pager['offset'])
        request.session['photo_albums_history'] = photo_albums.ids[:100]
        
       
        values.update({
            'photo_albums': photo_albums,
            'page_name': 'photo_albums_page',
            'pager': pager,
            'default_url': '/photo/albums',
        })
        return request.render("gadr_website.portal_photo_albums", values)
    
    @http.route(['/photo/albums/<int:album_id>','/photo/albums/<int:album_id>/page/<int:page>'], type='http', auth="public", website=True)
    def portal_photo_albums_detail(self, album_id=None, page=1, access_token=None,  **kw):
        
        try:
            values = self._prepare_portal_layout_values()
            PhotoAlbums = request.env['gadr.media.media.line']
            domain =[('media_id', '=' , album_id)]
            # default sort by order
           
            photo_count = PhotoAlbums.search_count(domain)
            pager = portal_pager(
                url="/photo/albums/%s" % (album_id),
                url_args={'album_id': album_id},
                total=photo_count,
                page=page,
                step=6
            )
            # content according to pager and archive selected
            photo_albums = PhotoAlbums.search(domain, order='create_date desc', limit=6, offset=pager['offset'])
            request.session['photo_album_history'] = photo_albums.ids[:100]
            
            values.update({
                'photo_albums_line': photo_albums,
                'page_name': 'photo_album_page',
                'pager': pager,
                'default_url': '/photo/albums/%s' % (album_id),
                'album_id': album_id,
                })
                   
        except (AccessError, MissingError):
            return request.redirect('/photo/albums')
        
        return request.render("gadr_website.portal_photo_albums_infos", values)