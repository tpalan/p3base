from odoo import models, fields, _


class ProductProductInherit(models.Model):
    _inherit = 'product.product'
    partner_ref = fields.Char(compute='_product_partner_ref', string='Customer ref')

    def _product_partner_ref(self):
        for p in self:
            p.partner_ref = p.name
