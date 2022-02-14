# -*- coding: utf-8 -*-
from odoo import http

# class Crm-qualifications(http.Controller):
#     @http.route('/crm-qualifications/crm-qualifications/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm-qualifications/crm-qualifications/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm-qualifications.listing', {
#             'root': '/crm-qualifications/crm-qualifications',
#             'objects': http.request.env['crm-qualifications.crm-qualifications'].search([]),
#         })

#     @http.route('/crm-qualifications/crm-qualifications/objects/<model("crm-qualifications.crm-qualifications"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm-qualifications.object', {
#             'object': obj
#         })