# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WizardLibraryBookRent(models.TransientModel):

    _name = 'wizard.library.book.rent'
    _inherit = 'library.book.rent.abstract'

    count_book_rented = fields.Integer(
        related='partner_id.count_book_rented'
    )

    line_ids = fields.One2many(
        comodel_name='wizard.library.book.rent.line',
        inverse_name='rent_id',
    )

    @api.onchange('book_asset_id')
    def _onchange_book_asset_id(self):

        for record in self:
            if record.book_asset_id:
                #
                # Tomar cuidado para não usar o CREATE ao Invez do NEW!!!!!

                record.line_ids |= record.line_ids.new({
                    'rent_id': record.id,
                    'book_asset_id': record.book_asset_id.id
                })

                # Outra possibilidade
                # https://github.com/kmee/l10n-brazil/blob/8.1/l10n_br_account_product/models/account_invoice_payment.py
                # item_ids = [
                #     (5, 0, {})
                # ]
                # https://stackoverflow.com/a/39896208
                # record.line_ids = [(0, 0, {
                #     'rent_id': record.id,
                #     'book_asset_id': record.book_asset_id.id
                # })]

                record.book_asset_id = False

    @api.multi
    def doit(self):
        for wizard in self:
            # Active model!: Modelo que esta atras do wizard
            # Active ID: Id do modelo que esta atras do wizard
            # Active IDS: Através da visão lista, lista dos registros selecionados.
            rent_id = self.env['library.book.rent']
            for line in wizard.line_ids:
                rent_id |= self.env['library.book.rent'].create({
                    'partner_id': wizard.partner_id.id,
                    'book_asset_id': line.book_asset_id.id,
                })
            rent_id.action_rent()

        # View dinamicamente para um modelo.
        # action = {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Livros Alugados',
        #     'res_model': 'library.book.rent',
        #     'domain': [('id', '=', rent_id.id)],
        #     'view_mode': 'tree,form',
        # }

        if self.env.context.get('save_and_create'):
            action = self.env.ref('library_base.wizard_library_book_rent_act_window').read()[0]
        else:
            action = self.env.ref('library_base.library_book_rent_act_window').read()[0]
            rent_ids = self.env['library.book.rent'].search([
                ('partner_id', '=', wizard.partner_id.id),
            ])
            action['domain'] = [('id', 'in', rent_ids.ids)]
        return action


class WizardLibraryBookRentLine(models.TransientModel):

    _name = 'wizard.library.book.rent.line'

    _rec_name = 'book_asset_id'

    rent_id = fields.Many2one(
        comodel_name='wizard.library.book.rent'
    )

    book_asset_id = fields.Many2one(
        string="Tombamento",
        comodel_name='library.book.asset',
    )
