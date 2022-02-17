# -*- coding: utf-8 -*-
{
    'name': "CRM Qualifications",

    'summary': """
        This addon adds features to the CRM app""",

    'description': """
        Long description of module's purpose
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
        'views/custom_lead_views.xml',
        'views/custom_partner_views.xml',
        'report/report.xml',
        'report/report_overdue_actions_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}