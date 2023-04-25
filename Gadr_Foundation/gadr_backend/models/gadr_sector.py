import hashlib
from odoo import api, fields, models, _


class GadrProjects(models.Model):
    _name = 'gadr.sector'
    _description = 'Gadr Sector'

    name_en= fields.Char('Name En')
    name_ar = fields.Char('Name Ar')
    binary_file  = fields.Image(string="Imge")
    projects_event_id = fields.Many2one("gadr.projects.event")
    
    def name_get(self):
        result = []
        for record in self:
            lang = self.env.user.lang
            if lang == 'en_US':
                name = "Sector {}".format(record.name_en)
            else:
                name = "القطاع {}".format(record.name_ar)
            result.append((record.id, name))
        return result
    
    @api.model
    def image_url(self, record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)