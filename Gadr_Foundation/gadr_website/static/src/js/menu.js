odoo.define("gadr_website.menu", function(require) {
    "use strict";

    const { extraMenuUpdateCallbacks } = require("website.content.menu");
    var publicWidget = require("web.public.widget");

    publicWidget.registry.StandardAffixedHeader.include({
        /**
        //      * @constructor
        //      */
        init: function() {

            // var h = window.innerHeight;
            this._super(...arguments);
        },

        /**
         * Adapt the 'right' css property of the header by adding the size of a
         * scrollbar if any.
         *
         * @private
         */
        _adaptFixedHeaderPosition() {
            // Compensate scrollbar
            this.el.style.removeProperty("right");
            if (this.fixedHeader) {
                console.log("Scrollbar", this)
                const scrollableEl = $(this.el).parent().closestScrollable()[0];
                const style = window.getComputedStyle(this.el);
                const borderLeftWidth = parseInt(style.borderLeftWidth.replace('px', ''));
                const borderRightWidth = parseInt(style.borderRightWidth.replace('px', ''));
                const bordersWidth = borderLeftWidth + borderRightWidth;
                const newValue = parseInt(style['right']) + scrollableEl.offsetWidth - scrollableEl.clientWidth - bordersWidth;
                this.el.style.setProperty('left', `${newValue}px`, 'important');
            }
        },
    });
});