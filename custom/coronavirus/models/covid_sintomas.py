from odoo import models, fields, api


class CovidSintomas(models.Model):
    _name = 'covid.sintomas'
    _description = 'Sintomas Covid'

    name = fields.Char('Sintoma')



