# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class VisitorPartner(models.Model):
    
    _inherit = 'res.partner'
    
    is_visitor  = fields.Boolean()
    