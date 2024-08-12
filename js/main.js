function sendSequence() {
    $("#results").hide();
    $("#results").empty();

    var frmStr = $("#peptide_form").serialize();

    $.ajax({
        url: "./main.cgi",
        type: "POST",
        dataType: "json",
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform protein analysis! textStatus: (" + textStatus +") and errorThrown: ("+ errorThrown + ")");
        }
    });
}

function processJSON( data ) {
    $("#results").append("<p><strong>Sequence:</strong> " + data.sequence + "</p>");
    $("#results").append("<p><strong>Length:</strong> " + data.length + " amino acids</p>");
    $("#results").append("<p><strong>Weight:</strong> " + data.weight + " daltons</p>");
    $("#results").append("<p><strong>Hydropathy:</strong> " + data.hydropathy + "</p>");
    $("#results").append("<p><strong>Extinction Coefficient:</strong> " + data.extinction + "M-1cm-1</p>");
    $("#results").append("<p><strong>Charge at pH 7.4:</strong> " + data.pH_74 + "</p>");
    $("#results").append("<p><strong>pI:</strong> " + data.pI + "</p>");
    $("#results").show();
}

$(document).ready(function() {
    $("#submit").click(function(event) {
        event.preventDefault();
        sendSequence();
    });
});
