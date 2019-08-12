$(document).ready(function () {
// SLIDER
    $('.slider').slick({
        dots: false,
        infinite: true,
        speed: 500,
        fade: true,
        autoplay: true,
        autoplaySpeed: 3000,
        cssEase: 'linear',
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    dots: false
                }
            },
            {
                breakpoint: 551,
                settings: {
                    dots: true,
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

// SLIDER2
    $('.slider2').slick({
        arrows: false,
        dots: false,
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: false,
        speed: 500,
        cssEase: 'linear',
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    dots: false
                }
            },
            {
                breakpoint: 551,
                settings: {
                    dots: true,
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

// KABINET-OPEN
    $(document).on('click', '.tog-ln', function () {
        $(this).toggleClass('active');
        $($(this).data('show')).fadeToggle();
    });

    $(document).on('click', '.comments-js, .answer-counter', function () {
        var comment = $(this).next($(this).data('show'));
        $(this).toggleClass('active');
        comment.slideToggle();
    });


// RUBRIKI-SHOW
    $('.rubriki .download-more a').click(function () {
        event.preventDefault();
        var rubriki = $('.rubriki-show');
        if (rubriki.is(':hidden')) {
            rubriki.slideDown();
            $(this).fadeOut();
        }
    });

        var burger = document.querySelector('.burger-container'),
        header = document.querySelector('.mobile-header');

    burger.onclick = function () {
        header.classList.toggle('menu-opened');
    }
});
// TABS
$(document).ready(function () {
    // $(".tabs").lightTabs();
});
(function ($) {
    jQuery.fn.lightTabs = function (options) {

        var createTabs = function () {
            tabs = this;
            i = 0;

            showPage = function (i) {
                $(tabs).children("div").children("div").hide();
                $(tabs).children("div").children("div").eq(i).show();
                $(tabs).children("ul").children("li").removeClass("active");
                $(tabs).children("ul").children("li").eq(i).addClass("active");
            };

            showPage(0);

            $(tabs).children("ul").children("li").each(function (index, element) {
                $(element).attr("data-page", i);
                i++;
            });

            $(tabs).children("ul").children("li").click(function () {
                showPage(parseInt($(this).attr("data-page")));
            });
        };
        return this.each(createTabs);
    };
})(jQuery);

// MOBILE-HEADER
(function () {

}());

// POP-UP
$(document).on('click', '.button', function (e) {
    e.preventDefault();
    var data = $(this).attr('data-id');
    $('.overlay').fadeIn('fast', function () {
        $('#' + data).animate({'top': '50px'}, 500);
    });
});

$(document).on('click', '.box-close.one, .overlay', function (e) { // êëèêàåì ïî ýëåìåíòó êîòîðûé âñ¸ ýòî áóäåò çàêðûâàòü
    e.preventDefault();
    closeBox();

});

function closeBox() {
    $('.nonebox').animate({'top': '-1100px'}, 500, function () { // óáèðàåì íàø áëîê
        $('.overlay').fadeOut('fast'); // è òåïåðü óáèðàåì îâåðëýé
    });
}

