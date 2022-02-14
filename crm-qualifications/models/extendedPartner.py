from odoo import models, fields, api


class ExtendedPartner(models.Model):
    _inherit = 'res.partner'

    lead_ids = fields.One2many('crm.lead', 'partner_id', string="Leads")

    @api.multi
    def create_new_lead(self):
        return {
            'name': 'Create New Lead',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            # 'res_id': ,
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('crm-qualifications.wizard_create_lead').id,
            'context': {'default_partner_id': self.id, 'default_type': 'lead'}
        }
