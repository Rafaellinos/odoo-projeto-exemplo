# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    partner_relation_id = fields.Many2one(
        comodel_name='library.partner.relation',
        string="Tipo de Vinculo",
        index=True,
    )

    # Alunos, Professores, Servidores ( Bibliotecários);

    is_internal = fields.Boolean("Tem vinculo com a Universidade")

    book_rent_ids = fields.One2many(
        comodel_name='library.book.rent',
        inverse_name='partner_id'
    )

    count_book_rented = fields.Integer(
        compute='_compute_library_book'
    )
    count_book_all = fields.Integer(
        compute='_compute_library_book'
    )

    @api.depends('book_rent_ids')
    def _compute_library_book(self):
        for record in self:
            record.count_book_rented = self.env['library.book.rent'].search_count([
                ('partner_id', '=', record.id),
                ('state', '=', 'rented'),
            ])
            record.count_book_all = self.env['library.book.rent'].search_count([
                ('partner_id', '=', record.id),
            ])
            # record.count_book_rent = len(record.book_rent_ids.filtered(
            #     lambda s: s.state == 'rented'
            # ))

    @api.multi
    def action_view_partner_rented_books(self):
        self.ensure_one()
        action = self.env.ref('library_base.library_book_rent_act_window').read()[0]
        action['domain'] = [('partner_id', '=', self.id), ('state', '=', 'rented')]
        return action

    @api.multi
    def action_view_partner_all_books(self):
        self.ensure_one()
        action = self.env.ref('library_base.library_book_rent_act_window').read()[0]
        action['domain'] = [('partner_id', '=', self.id)]
        return action