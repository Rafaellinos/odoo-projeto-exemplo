# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class LibraryPartnerRelation(models.Model):

    _name = 'library.partner.relation'
    _description = 'Tipos de vinculo'

    name = fields.Char()
