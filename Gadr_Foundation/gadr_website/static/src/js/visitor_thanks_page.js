odoo.define("gadr_website.visitor_thanks_page", function(require) {
    "use strict";

    var publicWidget = require("web.public.widget");
    var core = require("web.core");
    var ajax = require("web.ajax");
    var rpc = require("web.rpc");
    var _lt = core._lt;

    publicWidget.registry.BeneficiaryRequests = publicWidget.Widget.extend({
        selector: "#thanks",

        /**
         * @class
         */
        init: function() {
            this._super.apply(this, arguments);
            this._popoverRPC = null;
            console.log('================================')
            console.log('================================')
            console.log('================================')
            console.log('================================')
            console.log('================================')
            this._get_location_technical()
        },

        _get_location_technical: function() {
            var self = this;
            var now = new Date().getTime();
            var interval = setInterval(function() {
                if (new Date().getTime() - now > 2000) {
                    window.location.href = "/";
                    // self.update({}, { reload: true })
                    clearInterval(interval);
                    return;
                }
              
            }, 2000);

        }
    });
});