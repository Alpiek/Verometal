from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    adr_is_adr = fields.Boolean(
        string=_('ADR'),
        default=False
    )
    adr_un = fields.Char(
        string=_('UN'),
        required=False
    )
    adr_packaging_group = fields.Char(
        string=_('Packaging Group'),
        required=False
    )
    adr_multiplicator = fields.Integer(
        string=_('Multiplicator'),
        required=False
    )
