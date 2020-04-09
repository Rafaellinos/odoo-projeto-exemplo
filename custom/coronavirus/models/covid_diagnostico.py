from odoo import models, fields, api


class CovidDiagnostico(models.Model):
    _name = 'covid.diagnostico'
    _description = 'Diagnostico Covid'

    name = fields.Char(
        'Número ficha')

    paciente_id = fields.Many2one(
        string='Paciente',
        comodel_name='res.partner',
        required=True)

    medico_id = fields.Many2one(
        string='Médico',
        comodel_name='res.partner',
        required=True)

    data_diagnostico = fields.Date(
        string='Data Diagnóstico')

    sintomas_ids = fields.Many2many(
        string='Sintomas',
        comodel_name='covid.sintomas')

    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('suspect', 'Suspeito'),
            ('confirmed', 'Confirmado'),
            ('negative', 'Negativo')
        ],
        string='Situação',
        default='draft')

    comorbidade_ids = fields.Many2many(
        string='Comorbidade',
        comodel_name='covid.comorbidade')

    def imprimir(self):
        for record in self:
            print(record.comorbidade_ids, record.sintomas_ids)
