# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WizardLibraryBookReturn(models.TransientModel):

    _name = 'wizard.library.book.return'

    date = fields.Date(
        string="Data Devolução",
        default=fields.Date.context_today,
    )

    @api.multi
    def doit(self):
        for wizard in self:
            active_ids = self.env.context.get('active_ids')
            active_model = self.env.context.get('active_model')
            if active_model == 'library.book.rent' and active_ids:
                rent_ids = self.env[active_model].browse(active_ids)
                rent_ids.action_return(wizard.date)
        return {'type': 'ir.actions.act_window_close'}
