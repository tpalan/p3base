from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    bmd_id = fields.Char('BMD Id', size=10)
