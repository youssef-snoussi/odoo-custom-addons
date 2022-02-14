odoo.define('crm-qualifications.JsToCallWizard', function (require) {
"use strict";

var ListController = require('web.ListController');

var JsToCallWizard = ListController.include({
  renderButtons: function($node){
    this._super.apply(this, arguments);
    if (this.$buttons) {
      this.$buttons.on('click', '.cs_print_late_leads', this.action_to_call_wizard.bind(this));
      this.$buttons.appendTo($node);
    }
  },
  action_to_call_wizard: function(event) {
    event.preventDefault();
    var self = this;
    self.do_action({
        name: "Open a wizard",
        type: 'ir.actions.act_window',
        res_model: 'wizard_create_lead',
        view_mode: 'form',
        view_type: 'form',
        views: [[false, 'form']],
        target: 'new',
     });

  },
});
});