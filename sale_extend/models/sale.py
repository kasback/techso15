# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    objet = fields.Char('Objet')
    texte_en_tete = fields.Text("Texte d'entête")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_type = fields.Many2one(related='product_id.categ_id', string='Type')


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    currency_id = fields.Many2one('res.currency', 'Devise')
