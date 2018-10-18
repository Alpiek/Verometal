# -*- coding: utf-8 -*-
{
    'name': 'Module for ADR - hazardous chemicals',
    'version': '11.0.0.1.0.0',
    'description': """
    ADR module with Hazardous products picking report
    """,
    'author': "Alpiek",
    'website': "https://alpiek.nl/",
    'depends': [
        'product',
        'stock',
    ],
    'data': [
        'views/product_views.xml',
        'report/hazardous_report.xml',
    ],
    'application': False,
    'license': u'OPL-1',
}
