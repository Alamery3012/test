import hashlib
from odoo import api, fields, models, _

class GadrPartener(models.Model):
    _name = 'gadr.partner'
    _description = 'Gadr Partner'

    name_en= fields.Char('Name En')
    name_ar = fields.Char('Name Ar')
    binary_file  = fields.Image(string="Imge")
    
    def name_get(self):
        result = []
        for record in self:
            lang = self.env.user.lang
            if lang == 'en_US':
                name = "partenr {}".format(record.name_en)
            else:
                name = "الشريك {}".format(record.name_ar)
            result.append((record.id, name))
        return result
    
    def image_url(self, record, field, size=None):
        """ Returns a local url that points to the image field of a given browse record. """
        sudo_record = record.sudo()
        sha = hashlib.sha512(str(getattr(sudo_record, '__last_update')).encode('utf-8')).hexdigest()[:7]
        size = '' if size is None else '/%s' % size
        return '/web/image/%s/%s/%s%s?unique=%s' % (record._name, record.id, field, size, sha)
    