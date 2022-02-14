from odoo import models, fields, api


class ExtendedLeads(models.Model):
    _inherit = "crm.lead"

    action_date = fields.Date('Next Action Date')

    @api.multi
    def edit_action_date(self):
        return {
            'name': 'Edit Next Action Date',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            # 'res_id': self.id,
            'res_model': 'crm.lead',
            'type': 'ir.action.act_window',
            'view_id': self.env.ref('crm-qualifications.wizard_edit_action_date').id,
            'context': {'default_lead_id': self.id}
        }

    def define_action_date(self):
        return {
            'name': 'Expiration date',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id,
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('crm-qualifications.wizard_edit_action_date').id,
            'context': {'default_partner_id': self.id, 'default_type': 'lead'}
        }

    @api.multi
    def print_late_leads(self):
        print('report printed!')
