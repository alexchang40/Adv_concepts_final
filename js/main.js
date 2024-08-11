function sendSequence( input ) {
    $("#results").hide();
    $("tbody").empty();

    var frmStr = $("peptide_form").serialize();

    $.ajax({
        url: "./main.cgi",
        dataType: "json",
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            alert("It worked");
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform protein analysis! textStatus: (" + textStatus +") and errorThrown: ("+ errorThrown + ")");
        }
    });
}

function processJSON( data ) {
}

$("submit").click( function() {
    sendSequence();
    return false;
});
