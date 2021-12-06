# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    client_id = fields.Many2one('res.partner', 'Client')
