from odoo import api, fields, models, _


class Typology(models.Model):
    _name = 'typology'

    name = fields.Char(
        string=_('Name'),
        required=True
    )
    color = fields.Integer(
        string='Color Index'
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
        string=_('Linked Businesses')
    )
    typology = fields.Many2many(
        'typology',
        string=_('Typology')
    )
