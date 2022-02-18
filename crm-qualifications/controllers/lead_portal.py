from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http
from odoo.http import request
from datetime import date
from odoo import _


class LeadPortal(CustomerPortal):

    def get_lead_domain(self):
        return [
            ('user_id', '=', request.env.user.id),
            ('next_action_date', '<', date.today()),
            ('type', '=', 'lead')
        ]

    def _prepare_portal_layout_values(self):
        values = super(LeadPortal, self)._prepare_portal_layout_values()
        lead_count = request.env['crm.lead'].search_count(self.get_lead_domain())
        values.update({
            'lead_count': lead_count,
        })
        return values

    @http.route(['/my/overdue_leads', '/my/overdue_leads/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_overdue_leads(self, page=1, date_begin=None, date_end=None, sortby=None, **kwargs):
        
        values = self._prepare_portal_layout_values()
        CrmLead = request.env['crm.lead']
        domain = self.get_lead_domain()

        searchbar_sortings = {
            'action_date': {'label': _('Due Date'), 'order': 'next_action_date asc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }

        # default sort bu value
        if not sortby:
            sortby = 'action_date'
        order = searchbar_sortings[sortby]['order']

        # archive groups - Default Group By 'create_date'
        archive_groups = self._get_archive_groups('crm.lead', domain)
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
        # pager
        lead_count = CrmLead.search_count(domain)
        pager = request.website.pager(
            url="/my/overdue_leads",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=lead_count,
            page=page,
            step=self._items_per_page
        )      

        # content according to pager and archive selected
        leads = CrmLead.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])

        values.update({
            'date': date_begin,
            'leads': leads,
            'page_name': 'overdue_leads',
            'archive_groups': archive_groups,
            'default_url': '/my/overdue_leads',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("crm-qualifications.portal_my_overdue_leads", values)