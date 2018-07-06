from odoo import api, fields, models, _


class Typology(models.Model):
    _name = 'x_typology'

    name = fields.Char(
        string=_('Name'),
        required=True
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    v_parent_id = fields.Many2one(
        'res.partner',
        string=_('Business Partner'),
        required=False
    )
    v_child_ids = fields.One2many(
        'res.partner',
        'v_parent_id',
        string=_('Link Businesses')
    )
    x_typology = fields.Many2many(
        'x_typology',
        string=_('Typology')
    )
