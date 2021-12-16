# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_footer_text(self):
        return """
            <p class="terms" style="color: rgb(68, 75, 90);">
                <span style="font-weight: bolder;">Conditions de paiement</span>: Payable à la Facturation
            </p>
            <p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Mode de règlement: </span>Virement</p>
            <p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Date d'écheance: </span></p>
            <p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Coordonnées bancaires:</span>&nbsp;ATTIJARIWAFA BANK</p>
            <p style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Coordonnées bancaires:&nbsp;</span>Compte N°MA 64 007 780 8003004000000545 79</p>
            <p style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Coordonnées bancaires:&nbsp;</span>SWIFT N°&nbsp;BCMAMAMC</p>
        """

    footer_text = fields.Html('Informations suplémentaires', default=get_footer_text)
