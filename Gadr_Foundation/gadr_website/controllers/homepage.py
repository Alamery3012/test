# -*- coding: utf-8 -*-

import base64
import hashlib

from odoo.tools.image import image_guess_size_from_field_name
from odoo import _, http
from odoo.http import request, route
from odoo.exceptions import AccessError, UserError
from odoo.addons.portal.controllers.portal import CustomerPortal


def _get_image(record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)

class HomePage(CustomerPortal):
    @http.route(['/web/attachment/<string:model>/<int:id>/<string:field>'], type='http', auth="public")
    # pylint: disable=redefined-builtin,invalid-name
    def content_image_gadr(self, xmlid=None, model='ir.attachment', id=None, field='raw',
                      filename_field='name', filename=None, mimetype=None, unique=False,
                      download=False, width=0, height=0, crop=False, access_token=None,
                      nocache=False):
        try:
            record = request.env['ir.binary']._find_record(xmlid, model, id and int(id), access_token)
            stream = request.env['ir.binary']._get_image_stream_from(
                record, field, filename=filename, filename_field=filename_field,
                mimetype=mimetype, width=int(width), height=int(height), crop=crop,
            )
        except UserError as exc:
            if download:
                raise request.not_found() from exc
            # Use the ratio of the requested field_name instead of "raw"
            if (int(width), int(height)) == (0, 0):
                width, height = image_guess_size_from_field_name(field)
            record = request.env.ref('web.image_placeholder').sudo()
            stream = request.env['ir.binary']._get_image_stream_from(
                record, 'raw', width=int(width), height=int(height), crop=crop,
            )

        send_file_kwargs = {'as_attachment': download}
        if unique:
            send_file_kwargs['immutable'] = True
            send_file_kwargs['max_age'] = http.STATIC_CACHE_LONG
        if nocache:
            send_file_kwargs['max_age'] = None

        return stream.get_response(**send_file_kwargs)
    
    @route(["/",'/my'], type="http", auth="public", website=True)
    def home(self, **kw):
        values = self._prepare_portal_layout_values()
        values.update({
            'page_name': 'home',
            'carousel_slide':  self.get_value_modl('gadr.projects.event',limit=5),
            'gadr_projects': self.get_value_modl('gadr.projects.event',self.get_domain('type','projects'), limit=10),
            'gadr_event': self.get_value_modl('gadr.projects.event',self.get_domain('type','event'), limit=10),
            'photo_albums': self.get_value_modl('gadr.media.media',self.get_domain('type','photo_albums'), 6),
            'video_albums': self.get_value_modl('gadr.media.media',self.get_domain('type','video_albums'), 6),
            'gadr_sector': self.get_value_modl('gadr.sector'),
            'gadr_partner': self.get_value_modl('gadr.partner'),
            # 'gadr_survey': self.get_value_modl('survey.survey'),
        })
       
        return request.render("gadr_website.homepage",values)
    
    
    def get_value_modl(self,mdoel, domain=[], limit=None):
        record_ids =  request.env[mdoel].sudo().search(domain,order='create_date desc', limit=limit)
       
        return record_ids

    def get_domain(self,keys, value):
        return [(keys, "=", value)]