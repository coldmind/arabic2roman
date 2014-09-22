var delay = (function(){
    var timer = 0;
    return function(callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();

$(document).ready(function() {
    $("#number").keyup(function() {
        delay(function(){
            var value = $("#number").val();
            if(value === "") {
                $("#result").val('');
                return false;
            }

            $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({number: $("#number").val()}),
                dataType: 'json',
                url: '/convert_number/',
                success: function (data){
                    $('#error').hide();
                    $("#result").val(data.result);
                },
                error: function(error) {
                    $("#result").val('');
                    $('#error').show().text(error.responseJSON.message);
                }
            });
        }, 150);
    });
});
