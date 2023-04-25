import hashlib
from odoo import api, fields, models, _


class GadrMediaMedia(models.Model):
    _name = 'gadr.media.media'
    _description = 'Gadr Media Media'
    _rec_name = 'name_album_en' 
      
    name_album_en = fields.Char('Name Album En')
    name_album_ar = fields.Char('Name Album Ar')
    binary_file = fields.Binary(attchment=True)
    type = fields.Selection([('video_albums', 'Video Albums'), ('photo_albums', 'Photo Albums')]) 
    media_line_ids = fields.One2many('gadr.media.media.line', 'media_id', copy=True)
    
    @api.model
    def image_url(self, record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)
    
    
class GadrMediaMedia(models.Model):
    _name = 'gadr.media.media.line'
   
    binary_file = fields.Binary(attchment=True)
    media_id = fields.Many2one('gadr.media.media')
    link_video = fields.Char()
    projects_id = fields.Many2one('gadr.projects.event')
    type = fields.Selection(related='media_id.type', store=True,)