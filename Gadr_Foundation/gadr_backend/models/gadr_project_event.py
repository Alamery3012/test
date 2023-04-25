import hashlib
from odoo import api, fields, models, _


class GadrProjects(models.Model):
    _name = 'gadr.projects.event'
    _description = 'Gadr Projects'

    name = fields.Char('Reference', index=True, required=True, readonly=True, default=_('New'))
    type = fields.Selection([('projects', 'Projects'), ('event', 'event')]) 
    title_en = fields.Char()
    title_ar = fields.Char()
    sector_ids = fields.Many2many("gadr.sector", 'projects_event_id') 
    binary_file  = fields.Binary(string="Imge")
    date = fields.Date()
    description_en = fields.Text()
    description_ar = fields.Text()
    media_line_ids = fields.One2many('gadr.media.media.line', 'projects_id', copy=True)
    
    @api.model
    def image_url(self, record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)
    
    @api.model
    def create(self, vals):
        type = self._context.get('default_type')
        if type == 'projects' or vals.get('type') == 'projects':
            vals['name'] = self.env['ir.sequence'].next_by_code('gadr.projects.code') or _('New')
        elif type == 'event' or vals.get('type') == 'event':
            vals['name'] = self.env['ir.sequence'].next_by_code('gadr.event.code') or _('New')
      
       
        return super(GadrProjects, self).create(vals)