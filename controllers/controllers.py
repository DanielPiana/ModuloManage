# -*- coding: utf-8 -*-
# from odoo import http


# class Managedaniel(http.Controller):
#     @http.route('/managedaniel/managedaniel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managedaniel/managedaniel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managedaniel.listing', {
#             'root': '/managedaniel/managedaniel',
#             'objects': http.request.env['managedaniel.managedaniel'].search([]),
#         })

#     @http.route('/managedaniel/managedaniel/objects/<model("managedaniel.managedaniel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managedaniel.object', {
#             'object': obj
#         })
