# -*- coding: utf-8 -*-
{
    'name': 'Verometal customizations',
    'version': '11.0.0.1.0.0',
    'description': """
    Verometal customizations.
    """,
    'author': "Alpiek",
    'website': "https://alpiek.nl/",
    'depends': [
        'contacts',
        'mail',
        'sales_team',
    ],
    'data': [
        'views/mail_views.xml',
        'views/partner_views.xml',
        'security/ir.model.access.csv'
    ],
    'application': False,
    'license': u'OPL-1',
}
