$(document).ready(function(){
  $('#sub1').click(function(){
  showpopup2();
  //return false;
  });   
});

$(document).ready(function(){
  $('#sub2').click(function(){
  showpopup1();
  //return false;
  });   
});

$(document).ready(function(){
	$('#show_signin').click(function(){
	showpopup1();
	//return false;
	});		
});


$(document).ready(function(){
  $('#show_signinback').click(function(){
  showpopup1();
  //return false;
  });   
});


function showpopup2()
{
   $("#loginform").fadeIn();
   $("#signupform").fadeOut();
    $("#signupform").css({"visibility":"hidden","display":"none"});
    $("#loginform").css({"visibility":"visible","display":"block"});
    // $('.dropdown-menu').slideDown();
    $('myDropDown *').click(function(e) {
    e.stopPropagation();
});
}

function showpopup1()
{
   $("#loginform").fadeIn();
   $("#signupform").fadeOut();
    $("#signupform").css({"visibility":"hidden","display":"none"});
    $("#loginform").css({"visibility":"visible","display":"block"});
    $('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});
}

$(document).ready(function(){
	$('#show_signup').click(function(){
	showpopup();
	//return false;
	});		
});
function showpopup()
{
   $("#loginform").fadeOut();
   $("#signupform").fadeIn();
    $("#loginform").css({"visibility":"hidden","display":"none"});
   $("#signupform").css({"visibility":"visible","display":"block"});
   $('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});
}

$(document).ready(function(){
  $('#change_pass').click(function(){
  showpopup10();
  //return false;
  });   
});

function showpopup10()
{
   $("#logoutform").fadeOut();
   $("#passchangeform").fadeIn();
    $("#logoutform").css({"visibility":"hidden","display":"none"});
   $("#passchangeform").css({"visibility":"visible","display":"block"});
   $('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});
}


$(document).ready(function(){
  $('#show_signout').click(function(){
  showpopup11();
  //return false;
  });   
});

function showpopup11()
{
   $("#logoutform").fadeIn();
   $("#passchangeform").fadeOut();
    $("#passchangeform").css({"visibility":"hidden","display":"none"});
    $("#logoutform").css({"visibility":"visible","display":"block"});
    $('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});
}
