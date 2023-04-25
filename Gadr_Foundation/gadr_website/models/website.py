import logging

from odoo import models
from odoo.http import request

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = "website"

    def get_gadr_survey(self):
        survey = request.env['survey.survey'].sudo().search([],order='create_date desc')
        return survey