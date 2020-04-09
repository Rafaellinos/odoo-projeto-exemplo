# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

try:
    import isbn_hyphenate
    from is_isbn.is_isbn import is_isbn
except (ImportError, IOError) as err:
    _logger.info(err)

class ProductProduct(models.Model):

    _inherit = 'product.product'

    isbn = fields.Char(
        string='ISBN',
        copy=False,
    )
    author_ids = fields.Many2many(
        string="Author",
        comodel_name="res.partner",
        relation="book_author_rel",
        column1="product_id",
        column2="author_id",
        domain=[('is_author', '=', True)],
    )
    editor_id = fields.Many2one(
        string='Editor',
        comodel_name='res.partner',
        domain=[('is_publisher', '=', True)],
    )

    _sql_constraints = [
        ('isbn_uniq', 'unique (isbn)', 'The code of the ISBN musy be unique !')
    ]

    def _format_isbn(self):
        for record in self:
            if record.isbn:
                formatado = False
                try:
                    formatado = isbn_hyphenate.try_hyphenate(record.isbn)
                except:
                    pass
                finally:
                    if not formatado:
                        raise UserError("Length must be 10 or 13")
                    valido = is_isbn(formatado)
                    if not valido:
                        raise UserError("Isbn inválido")
                    record.isbn = formatado

    @api.onchange('isbn')
    def onchange_isbn(self):
        self._format_isbn()

    @api.constrains('isbn')
    def validate_isbn(self):
        for record in self:
            valido = is_isbn(record.isbn)
            if not valido:
                raise ValidationError(_("Isbn inválido"))

