# -*- coding: utf-8 -*-

{
    'name': u'Techsogroup -- Impression des Documents commerciaux',
    'version': '1.0',
    'summary': u'',
    'category': 'Gestion Commerciale',
    'author': 'Osisoftware',
    'website': '',
    'depends': [
        'base', 'web', 'sale'
    ],
    'data': [
        'report/export_report_sale_template.xml',
        'report/report.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
