var swiper = new Swiper('.gadr_project_event', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 2,
        slideShadows: true,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true,
    },


});
var swipers = new Swiper(".mySwiper", {
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

var swiper_sector = new Swiper(".Swiper-sector", {
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

var gadrsector = new Swiper(".gadr_sector", {

    slidesPerView: 1,
    spaceBetween: 10,
    freeMode: true,
    // loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        "@0.00": {
            slidesPerView: 'auto',
            spaceBetween: 2,
        },
        "@0.75": {
            slidesPerView: 5,
            spaceBetween: 20,
        },
        "@1.00": {
            slidesPerView: 7,
            spaceBetween: 40,
        },
        "@1.50": {
            slidesPerView: 9,
            spaceBetween: 50,
        },

    },
});

$(document).ready(function() {
    $('.scroll-top').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 100);
        return false;
    });

});

// $(window).scroll(function(){
//     var header = $('header');
//         scroll = $(window).scrollTop(); 
//     if (scroll >= 50) header.addClass('fixed');
//     else header.removeClass('fixed');
//     if (scroll >= 25) header.addClass('navScroll');
//     else header.removeClass('navScroll');
//   });