from odoo import models, fields, api


class CustomPartner(models.Model):
    _inherit = 'res.partner'

    # A variable to store customers' lead
    lead_ids = fields.One2many('crm.lead', 'partner_id', string="Leads")

    # Defining a function to call a wizard
    @api.multi
    def create_new_lead(self):
        return {
            'name': 'Create New Lead',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('crm-qualifications.wizard_create_lead').id,
            'context': {'default_partner_id': self.id, 'default_type': 'lead'}
        }