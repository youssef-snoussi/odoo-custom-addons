# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/crm-qualifications(http.Controller):
#     @http.route('/custom-addons/crm-qualifications/custom-addons/crm-qualifications/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/crm-qualifications/custom-addons/crm-qualifications/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/crm-qualifications.listing', {
#             'root': '/custom-addons/crm-qualifications/custom-addons/crm-qualifications',
#             'objects': http.request.env['custom-addons/crm-qualifications.custom-addons/crm-qualifications'].search([]),
#         })

#     @http.route('/custom-addons/crm-qualifications/custom-addons/crm-qualifications/objects/<model("custom-addons/crm-qualifications.custom-addons/crm-qualifications"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/crm-qualifications.object', {
#             'object': obj
#         })