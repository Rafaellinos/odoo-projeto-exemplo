from odoo import models, fields, api, _


class CovidComorbidade(models.Model):
    _name = 'covid.comorbidade'
    _description = 'Comorbidade'
    _order = 'codigo_sid,name' # select ** from covid_comorbidade by 'order'
    #_rec_name = 'num' # para usar outro campo para aparecer, default é name

    _sql_constraints = [
        ('codigo_sid_uniq', 'UNIQUE (codigo_sid)', _("Código SID tem que ser único!"))]

    display_name = fields.Char(store=True) # store true para salvar no bd

    name = fields.Char(
        'Comorbidade')

    codigo_sid = fields.Char('Código SID')

    @api.multi # opcional todu método é multi por default
    def name_get(self):
    #def name_get(self) -> list:
        result = list()
        for record in self:
            if all([record.name, record.codigo_sid]):
                result.append((record.id, f"[{record.codigo_sid}]-{record.name}"))
            else:
                result.append((record.id, (record.name or record.codigo_sid)))
        return result
