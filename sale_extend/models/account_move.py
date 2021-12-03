# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_footer_text(self):
        return """
            <p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Conditions de paiement</span>: Payable à la commande</p><p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Mode de règlement :</span></p><p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Date d'écheance :</span></p><p class="terms" style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;">Coordonnées bancaires:</span>&nbsp;BMCE-BANK-CENTRE D’AFFAIRES ZENITH MILLENIUM</p><p style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;"><font class="text-white">Coordonnées bancaires:&nbsp;</font></span>Compte N°&nbsp;011780000529210000129035</p><p style="color: rgb(68, 75, 90);"><span style="font-weight: bolder;"><font class="text-white">Coordonnées bancaires:&nbsp;</font></span>SWIFT N°&nbsp;BMCEMAMC</p>
        """

    footer_text = fields.Html('Informations suplémentaires', default=get_footer_text)
