// for sticky btn if >=2 btn on page
function isOnScreen(elem) {
    // if the element doesn't exist, abort
    if (elem.length == 0) {
        return;
    }
    var $window = jQuery(window);
    var viewport_top = $window.scrollTop();
    var viewport_height = $window.height();
    var viewport_bottom = viewport_top + viewport_height;
    var $elem = jQuery(elem);
    var top = $elem.offset().top;
    var height = $elem.height();
    var bottom = top + height;

    return (top >= viewport_top && top < viewport_bottom) ||
        (bottom > viewport_top && bottom <= viewport_bottom) ||
        (height > viewport_height && top <= viewport_top && bottom >= viewport_bottom);
}

jQuery.fn.some = function (fn, thisArg) {
    var result;
    for (var i = 0, iLen = this.length; i < iLen; i++) {
        if (this.hasOwnProperty(i)) {
            if (typeof thisArg == 'undefined') {
                result = fn(this[i], i, this);
            } else {
                result = fn.call(thisArg, this[i], i, this);
            }
            if (result) return true;
        }
    }
    return false;
}

$(document).ready(function () {

    var swiper = new Swiper('#credit_cards_swiper_container', {
        // Default parameters
        slidesPerView: 3,
        spaceBetween: 40,
        loop: false,
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },
        // Responsive breakpoints
        breakpoints: {
            991: {
                slidesPerView: 5,
                spaceBetween: 50,
                centeredSlides: true,
                loop: true,
                autoplay: {
                    delay: 4000,
                    disableOnInteraction: false,
                },
            },
            520: {
                slidesPerView: 1,
                spaceBetween: 100,
                centeredSlides: true,
                loop: true,
                autoplay: {
                    delay: 1500,
                    disableOnInteraction: false,
                },
            }
        }
    })


    //////////////////////////////////////////////

    $('.scroll-to-element').click(function(e){
        e.preventDefault();
        setTimeout(function(){
            $("html, body").animate({scrollTop: $(".form_section").offset().top - 100}, 500)
        },200);
    });


    if (window.matchMedia('(max-width:991px)').matches ) {
        var stickyCTA = $('.block-sticky');

        $('.floating_risks_wrapper').prepend( stickyCTA );

        sticky_btn()

        $(window).scroll(function() {
            sticky_btn();
        });

        $(window).resize(function () {
            sticky_btn();
        });

        function sticky_btn() {
            if (window.matchMedia('(max-width:991px)').matches) {
                if ($('.sticky-no').some(isOnScreen)) {
                    $(".block-sticky").hide();
                } else {
                    $(".block-sticky").show();
                }
            } else {
                $(".block-sticky").hide();
            }
        }

    }


    // alvexo_plus_section
    var qurery = '?autoplay=1&loop=1&autopause=0&muted=1&quality=1080p'
    var videos = {
        signals: {web:'491681439',mobile:'497630033'},
        news:{web:'492071957',mobile:'497630006'},
        webTV:{web:'492071861',mobile:'497629966'},
        economic:{web:'491681388',mobile:'497629927'}
    }
    function setVideoByScreenWidth(x) {
        for(var type in videos){
            $('.alvexo_plus_section .'+ type +' iframe').attr("src", "https://player.vimeo.com/video/" + videos[type][(x.matches ? 'mobile' : 'web')] + qurery);
        }
    }

    var x = window.matchMedia("(max-width: 767px)")
    setVideoByScreenWidth(x)
    x.addListener(setVideoByScreenWidth)


    $('.alvexo_plus_section li').click(function(){
        var myClass = this.classList[0].toString();
        $('.alvexo_plus_section .active').removeClass('active');
        $('.alvexo_plus_section .'+myClass).toggleClass('active');
    });
});

var lang = location.origin.split('.')[2];   //  check lang




// animation title

var typedTextSpan = document.querySelector(".typed-text");
var cursorSpan = document.querySelector(".cursor");
var textArray = ["الأسهم", "العملات", "السلع", "المؤشرات"];

var typingDelay = 200;
var erasingDelay = 100;
var newTextDelay = 1000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
    if (charIndex < textArray[textArrayIndex].length) {
        if (!cursorSpan.classList.contains("typing"))
            cursorSpan.classList.add("typing");
        typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
    } else {
        cursorSpan.classList.remove("typing");
        setTimeout(erase, newTextDelay);
    }
}

function erase() {
    if (charIndex > 0) {
        if (!cursorSpan.classList.contains("typing"))
            cursorSpan.classList.add("typing");
        typedTextSpan.textContent = textArray[textArrayIndex].substring(
            0,
            charIndex - 1
        );
        charIndex--;
        setTimeout(erase, erasingDelay);
    } else {
        cursorSpan.classList.remove("typing");
        textArrayIndex++;
        if (textArrayIndex >= textArray.length) textArrayIndex = 0;
        setTimeout(type, typingDelay + 1100);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // On DOM Load initiate the effect
    if (textArray.length) setTimeout(type, newTextDelay + 250);
});


// change title warning words AR
function checkRiskLangId(){
    if( lang =='ae' ) {
        textArray.splice(0, 4, "Ø§Ù„Ø£Ø³Ù‡Ù…", "Ø§Ù„Ø¹Ù…Ù„Ø§Øª", "Ø§Ù„Ù…Ø¤Ø´Ø±Ø§Øª", "Ø§Ù„Ø³Ù„Ø¹");
    }else{}
}
$(".typed-text").append(checkRiskLangId());


function append_form() {
    if (window.matchMedia('(max-width:991px)').matches ) {
        if ($(".form_section_mobile input").length == 0) {
            $('.form_section').appendTo('.form_section_mobile .container');
        }
    } else {
        $('.form_section').appendTo('.form_section_desktop');
    }
}
append_form();

$(window).resize(function(){
    append_form();
});