$(document).ready(function(){
/* Set the width of the side navigation to 250px */
/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
    $('#open_navbar').click(function(){
        $('#mySidenav').css('width','300px');
        $('#main').css('margin-left', '250px');
        $('body').css('background-color','rgba(39, 38, 38, 0.212)');
    });

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
    $('#close_navbar').click(function(){
        $('#mySidenav').css('width','0');
        $('#main').css('margin', '0');
        $('body').css('background-color','white');
    });

})
