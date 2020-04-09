# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_publisher = fields.Boolean("É editor")
    is_author = fields.Boolean("É autor")

    author_book_ids = fields.Many2many(
        comodel_name="product.product",
        relation="book_author_rel",
        column1="author_id",
        column2="product_id",
    )
    editor_book_ids = fields.One2many(
        comodel_name='product.product',
        inverse_name='editor_id',
        string='Editor_book_ids',
        required=False
    )
