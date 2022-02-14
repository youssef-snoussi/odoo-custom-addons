# -*- coding: utf-8 -*-
{
    'name': "CRM-Qualifications",

    'summary': """
        This is an extension of the CRM module 12.0, it adds some useful functionalities""",

    'description': """
        
    """,

    'author': "Youssef",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'crm',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/extendedLeadsView.xml',
        'views/extendedPartnerView.xml',
        'reports/report_action.xml',
        'views/assets_backend.xml',
    ],
    'qweb': [
        'static/src/xml/print_leads_button.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}