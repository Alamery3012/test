# -*- coding: utf-8 -*-
from odoo import _, http
from odoo.http import request, route
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class VideoAlbums(CustomerPortal):
    
        
    @http.route(['/video/albums', '/video/albums/page/<int:page>'], type='http', auth="public", website=True)
    def portal_video_albums(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        VideoAlbums = request.env['gadr.media.media']
        domain =[('type', '=','video_albums')]
                #searchbar sortings
        
        # count for pager
        video_albums_count = VideoAlbums.search_count(domain)
        # pager
        pager = portal_pager(
            url="/video/albums",
            total=video_albums_count,
            page=page,
            step=4
        )
        # content according to pager and archive selected
        video_albums = VideoAlbums.search(domain, order='create_date desc', limit=4, offset=pager['offset'])
        request.session['video_albums_history'] = video_albums.ids[:100]
        
       
        values.update({
            'video_albums': video_albums,
            'page_name': 'video_albums_page',
            'pager': pager,
            'default_url': '/video/albums',
        })
        return request.render("gadr_website.portal_video_albums", values)
    
    @http.route(['/video/albums/<int:album_id>','/video/albums/<int:album_id>/page/<int:page>'], type='http', auth="public", website=True)
    def portal_video_albums_detail(self, album_id=None, page=1, access_token=None,  **kw):
        
        try:
            values = self._prepare_portal_layout_values()
            VideoAlbums = request.env['gadr.media.media.line']
            domain =[('media_id', '=' , album_id)]
            # default sort by order
           
            video_count = VideoAlbums.search_count(domain)
            pager = portal_pager(
                url="/video/albums/%s" % (album_id),
                url_args={'album_id': album_id},
                total=video_count,
                page=page,
                step=6
            )
            # content according to pager and archive selected
            video_albums = VideoAlbums.search(domain, order='create_date desc', limit=6, offset=pager['offset'])
            request.session['photo_album_history'] = video_albums.ids[:100]
            
            values.update({
                'video_albums_line': video_albums,
                'page_name': 'video_album_page',
                'pager': pager,
                'default_url': '/video/albums/%s' % (album_id),
                'album_id': album_id,
                })
                   
        except (AccessError, MissingError):
            return request.redirect('/video/albums')
        
        return request.render("gadr_website.portal_video_albums_infos", values)