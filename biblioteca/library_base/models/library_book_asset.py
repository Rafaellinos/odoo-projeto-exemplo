# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class LibraryBookAsset(models.Model):

    _name = 'library.book.asset'
    _description = 'Library Book Asset'  # TODO

    # TODO: Sequencial unico para código do tombamento.

    name = fields.Char(readonly=True)

    book_id = fields.Many2one(
        comodel_name='product.product',
        string='Livro',
        required=True,
    )
    state = fields.Selection(
        selection=[
            ('avaliable', 'Disponível'),
            ('rented', 'Alugado'),
            # ('reserved', 'Reservado'),
        ],
        default='avaliable',
        required=True,
        readonly=True,
    )
    shelf = fields.Char(
        string="Prateleira",
    )
    session = fields.Char(
        string="Sessão",
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moeda',
        default=lambda self: self.env.user.company_id.currency_id,
    )
    price_unit = fields.Monetary(
        string="Valor da compra",
    )

    @api.model
    def create(self, vals):
        codigo = self.env['ir.sequence'].next_by_code('book.asset')
        vals['name'] = codigo
        return super(LibraryBookAsset, self).create(vals)