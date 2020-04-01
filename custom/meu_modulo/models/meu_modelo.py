# -*- coding: utf-8 -*-
from odoo import models, fields


class MeuModelo(models.Model):
    _name = 'meu.modelo' # pontos serão substituídos por _ e criado tabela no bd

    name = fields.Char(
        string='Nome completo')
    # os atributos da clase, serão o nome dos campos da tabela
    cpf = fields.Char(
        string='CPF')
    date = fields.Date(
        string="Data")
    partner_ids = fields.Many2many(
        string="Contato",
        comodel_name='res.partner')
