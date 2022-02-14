odoo.define('crm-qualifications.print_late_leads-report', function(require){
    "use strict";
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var Qweb = core.qweb;
    var PrintReport = AbstractAction.extend({
        events: {
            "click cs_print_late_leads": _PrintReport


    /*
        template: 'print_late_leads-report',
        events: {
            "click .cs_print_late_leads": function(){
                console.log('button pressed')
                var self = this;
                var def = this._rpc({
                    model: 'crm.lead',
                    method: 'print_late_leads',
                    args: [[]],
                })
                .then(function(res){
                    console.log("Success");
                });
            },
            core.action_registry.add('print_action', PrintReport);
        }
    })
});*/