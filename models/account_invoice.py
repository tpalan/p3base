from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'
    period = fields.Char('Benefit period', readonly=True, states={'draft': [('readonly', False)]})

    @api.constrains('period')
    def _validate_period(self):
        for invoice in self:
            if invoice.type == 'out_invoice' and (not invoice.period or len(invoice.period) == 0):
                raise ValidationError(_("Leistungszeitraum fehlt."))
