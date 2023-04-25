odoo.define("gadr_website.home", function(require) {
    "use strict";

    var publicWidget = require("web.public.widget");
    var rpc = require("web.rpc");;

    var counter = 0;
    var counter_invoice = 0;
    var js_cost_before_tax = 0;
    var invoice_list = []
    publicWidget.registry.websitehome = publicWidget.Widget.extend({
        selector: "#add_finaical",
        events: {
            'click .scroll-top': '_onClickscrolltop',
        },

          /**
         * @class
         */
          init: function() {
            this._super.apply(this, arguments);
            this._popoverRPC = null;
            $(window).scroll(function () {
                if ($(this).scrollTop() > 100) {
                    $('.scroll-top').fadeIn();
                } else {
                    $('.scroll-top').fadeOut();
                }
            });
        },

        _onClickscrolltop: function(ev) {
            $("html, body").animate({
                scrollTop: 0
            }, 100);
            return false;
        }

    });
});