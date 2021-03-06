# -*- coding: utf-8 -*-

{
    'name': u'Techsogroup -- Impression des Documents commerciaux',
    'version': '1.0',
    'summary': u'',
    'category': 'Gestion Commerciale',
    'author': 'Osisoftware',
    'website': '',
    'depends': [
        'base', 'web', 'sale', 'crm', 'account'
    ],
    'data': [
        'report/report_sale.xml',
        'report/export_report_sale_template.xml',
        'report/move_report_template.xml',
        'report/standard_report_sale_document.xml',
        'report/report.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
        'views/account_move_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
