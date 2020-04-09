# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class LibraryBookRent(models.Model):

    _name = 'library.book.rent'
    _inherit = 'library.book.rent.abstract'
    _description = 'Library Book Rent'  # TODO

    name = fields.Char()

    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('rented', 'Emprestado'),
            ('done', 'Finalizado'),
        ],
        default='draft',
        required=True,
        readonly=True,
    )
    partner_id = fields.Many2one(
        readonly=True,
        states={'draft': [('readonly', False)]}
    )
    partner_relation_id = fields.Many2one(
        readonly=True,
        states={'draft': [('readonly', False)]}
    )
    book_asset_id = fields.Many2one(
        readonly=True,
        states={'draft': [('readonly', False)]}
    )
    book_id = fields.Many2one(
        comodel_name='product.product',
        related='book_asset_id.book_id',
        store=True, # Por Padrão é False
        states={'draft': [('readonly', False)]}
    )
    policy_id = fields.Many2one(
        string="Politica de aluguel",
        states = {'draft': [('readonly', False)]}
    )
    start_date = fields.Date(
        readonly=True,
        states={'draft': [('readonly', False)]}
    )
    stop_date = fields.Date(
        string="Data Devolução",
        readonly=True,
        states={'draft': [('readonly', False)]}
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for record in self:
            if record.partner_id:
                record.partner_relation_id = record.partner_id.partner_relation_id

    def action_rent(self):
        self.write({
            'state': 'rented'
        })
        book_asset_id = self.mapped('book_asset_id')
        book_asset_id.write({
            'state': 'rented'
        })

    def action_return(self, date):
        self.write({
            'state': 'done',
            'stop_date': date,
        })
        book_asset_id = self.mapped('book_asset_id')
        book_asset_id.write({
            'state': 'avaliable'
        })