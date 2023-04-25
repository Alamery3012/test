# -*- coding: utf-8 -*-

import hashlib
from odoo import models, fields, api


class CarouselSlide(models.Model):
    _name = 'carousel.slide'
    # _inherit = ['gadr.projects.event']
    _description = 'Carousel Slide'
    
    name = fields.Char(string='Sequence', required=True,  readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('gadr.carousel.slide'))
    binary_file = fields.Binary('Imge',required=True)
    
    
    @api.model
    def image_url(self, record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)
