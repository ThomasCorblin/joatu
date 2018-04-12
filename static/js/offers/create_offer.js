$(document).ready(function(){
    $('#submit_offer').click(function(e){
        $.post('/rest_api/offers/', $('#form_offer').serialize())
        .done(function(data){
            alert('hello')
        });
        e.preventDefault();

    });
})
