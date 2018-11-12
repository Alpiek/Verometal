# -*- coding: utf-8 -*-
{
    'name': 'Verometal customizations',
    'version': '11.0.0.1.0.1',
    'description': """
    Verometal customizations.
    """,
    'author': "Alpiek",
    'website': "https://alpiek.nl/",
    'depends': [
        'contacts',
        'mail',
        'sales_team',
        'sale'
    ],
    'data': [
        'views/mail_views.xml',
        'views/partner_views.xml',
        'security/ir.model.access.csv',
        'report/sale_order_delivery_slip_report.xml'
    ],
    'application': False,
    'license': u'OPL-1',
}
