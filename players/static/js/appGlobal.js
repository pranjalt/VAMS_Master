/**
 * 
 */
function register()
{
alert("in register function");

console.log("bbbbbbbbbbb");
$.ajax({
	  method: "GET",
	  url: "/registration/",
	  data: {},
	  //async:false,
	})
	  .done(function( msg ) {
		console.log("KKK" + msg);
	    //alert( "Response: " + msg );
	    /*$('#mainPage').html('Registration');*/
		$('#mainPage').after('<div id="Registration"></div>')
		
	  });

console.log("aaaaaaaaa");

}

function tabHit()
{
	alert("In TabClick function");
	$( function() {
		  $('li').click( function() {
			$('navtab').css('background', 'gray');
		    $(this).css('background', 'white');
		    $(this).css('color', 'black');
		    //$('#mainPage').html('user_admin/PlayersRegistration');
		    window.location='login_admin/PlayersRegistration'
		  } );
		} );

}

function openRegistration()
{
	alert("test in Open Registration Form");
	$(function(){
		$('#mainPage').html('<div id="regsitrationForm"><div>');
	});
	

}



function get_registration_form()
{
	
}