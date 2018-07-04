from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    v_parent_id = fields.Many2one(
        'res.partner',
        string='Business Partner',
        required=False
    )
    v_child_ids = fields.One2many(
        'res.partner',
        'v_parent_id',
        string='Link Businesses'
    )
