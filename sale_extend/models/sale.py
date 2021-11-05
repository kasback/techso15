# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    objet = fields.Char('Objet')
    texte_en_tete = fields.Text("Objet")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_type = fields.Selection(related='product_id.type', string='Type')


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    currency_id = fields.Many2one('res.currency', 'Devise')
