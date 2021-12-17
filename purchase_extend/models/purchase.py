# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    client_id = fields.Many2one('res.partner', 'Client')

    @api.onchange('partner_id')
    def update_supplier_ref(self):
        self.partner_ref = self.partner_id.ref
