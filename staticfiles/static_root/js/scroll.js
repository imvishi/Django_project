$(document).ready(function() {
  
    // Fixa navbar ao ultrapassa-lo
    var navbar = $('#navbar-main'),
    istdiv=$('#ist'),
            distance = istdiv.offset().top,
        $window = $(window);

    $window.scroll(function() {
        if ($window.scrollTop() >= distance) {
            navbar.addClass('navbar navbar-default')
            //navbar.removeClass('navbar-fixed-top').addClass('navbar-fixed-top');
            $("body").css("padding-top", "70px");
        } else {
            navbar.removeClass('navbar navbar-default');
            $("body").css("padding-top", "0px");
        }
    });
});

$(document).ready(function(){

    $("#bottom_hold").mouseenter(function(){
    $("#scroll_img").fadeIn();
    });
    $("#bottom_hold").mouseleave(function(){
    $("#scroll_img").fadeOut();
    });

    $('#bottom_hold').on('click',function (e) {
        e.preventDefault();

        var target = this.hash;
        var $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            window.location.hash = target;
        });
    });
});
$(document).ready(function () {
    $('a[href="' + this.location.pathname + '"]').parent().addClass('active');
});

