# -*- coding: utf-8 -*-
# from odoo import http


# class Identityform(http.Controller):
#     @http.route('/identityform/identityform', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/identityform/identityform/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('identityform.listing', {
#             'root': '/identityform/identityform',
#             'objects': http.request.env['identityform.identityform'].search([]),
#         })

#     @http.route('/identityform/identityform/objects/<model("identityform.identityform"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('identityform.object', {
#             'object': obj
#         })
