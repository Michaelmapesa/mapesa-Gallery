$(document).ready(function(){
    var navbarCollapse=function (){
        if ($("#navMain").offset().top>100){
            $("#navMain").addClass("navbar-shrink");

        }else {
            $("#navMain").removeClass("navbar-shrink");
        }
    };
    navbarCollapse();
    $(window).scroll(navbarCollapse);
    $('.close-nav').click(function(){
        document.getElementById("sideNav").style.width="0";
    })
    $('.open-nav').click(function(){
        document.getElementById('sideNav').style.width='290px'
    })
})