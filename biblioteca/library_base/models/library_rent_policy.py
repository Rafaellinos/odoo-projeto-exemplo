# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class LibraryRentPolicy(models.Model):

    _name = 'library.rent.policy'
    _description = 'Library Rent Policy'  # TODO

    name = fields.Char(
        index=True,
        required=True,
    )
    partner_relation_id = fields.Many2one(
        comodel_name='library.partner.relation',
        string="Tipo de Vinculo",
        required=True,
        index=True,
    )
    quantity = fields.Integer(
        string="Quantidade de Livros",
        required=True,
        index=True,
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moeda',
        default=lambda self: self.env.user.company_id.currency_id,
    )
    amount_fee = fields.Monetary(
        # currency_field=currency_id,
        # Caso o modelo tenha um atributo, chamado currency_id, isto não é necessário
        #   Só é necessário caso você queira trocar o campo de currency
        string="Total da multa / por dia",
        index=True,
        required=True,
    )
    rent_days = fields.Integer(
        string="Dias de aluguel",
        index=True,
        required=True,
    )

    # core / addons / account / models / account_invoice.py: 347
    # amount_total_signed = fields.Monetary(string='Total in Invoice Currency', currency_field='currency_id',
    #     store=True, readonly=True, compute='_compute_amount',
    #     help="Total amount in the currency of the invoice, negative for credit notes.")
    # amount_total_company_signed = fields.Monetary(string='Total in Company Currency', currency_field='company_currency_id',
    #     store=True, readonly=True, compute='_compute_amount',
    #     help="Total amount in the currency of the company, negative for credit notes.")
    # currency_id = fields.Many2one('res.currency', string='Currency',
    #     required=True, readonly=True, states={'draft': [('readonly', False)]},
    #     default=_default_currency, track_visibility='always')
    # company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string="Company Currency", readonly=True)



