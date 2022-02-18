from odoo import models, fields, api, _

class CustomLead(models.Model):
    _inherit = 'crm.lead'

    next_action_date = fields.Date("Next Action Date")

    # Funtion to define next action date for recently entered lead

    @api.multi
    def define_next_action_date(self):
        return {
            'name': _('Next Action Date'),
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id,
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('crm-qualifications.wizard_define_action_date').id,
            'context': {'default_partner_id': self.id, 'default_type': 'lead'}
        }