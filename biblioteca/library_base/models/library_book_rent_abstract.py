# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class LibraryBookRent(models.AbstractModel):

    _name = 'library.book.rent.abstract'
    _description = 'Library Book Rent'  # TODO

    name = fields.Char()

    @api.depends('partner_id', 'partner_relation_id', 'start_date')
    def _compute_policy_id(self):
        for record in self:
            if record.partner_relation_id:
                policy_id = self.env['library.rent.policy'].search([
                    ('partner_relation_id', '=', record.partner_relation_id.id)
                ], limit=1)
                record.policy_id = policy_id

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Locatário",
        domain=[('is_internal', '=', True)],
        required=True,
        index=True,
    )
    partner_relation_id = fields.Many2one(
        comodel_name='library.partner.relation',
    )
    book_asset_id = fields.Many2one(
        string="Tombamento",
        comodel_name='library.book.asset',
        domain=[('state', '=', 'avaliable')],
    )
    policy_id = fields.Many2one(
        comodel_name='library.rent.policy',
        compute='_compute_policy_id',
        store=True,
        string="Politica de aluguel",
    )
    start_date = fields.Date(
        string="Data Aluguel",
        default=fields.Date.context_today,
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for record in self:
            if record.partner_id:
                record.partner_relation_id = record.partner_id.partner_relation_id
