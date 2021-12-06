# -*- coding: utf-8 -*-

{
    'name': u'Techsogroup -- Impression des Documents commerciaux (BC Achats)',
    'version': '1.0',
    'summary': u'',
    'category': 'Gestion Commerciale',
    'author': 'Osisoftware',
    'website': '',
    'depends': [
        'base', 'purchase',
    ],
    'data': [
        'report/report_purchase.xml',
        'report/po_custom_report_templates.xml',
        'report/report.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
