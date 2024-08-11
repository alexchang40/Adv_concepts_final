function submitForm() {
    const sequence = document.getElementById("sequence").value.trim();

    if (!sequence) {
        alert("Please enter a sequence!");
        return;
    }

    const formData = new FormData();
    formData.append("sequence", sequence);

    
    fetch("/../main.cgi", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let resultsHtml = "<h2>Results:</h2><ul>";
            for (const aa in data) {
                resultsHtml += `<li>${aa}: ${data[aa]}</li>`;
            }
            resultsHtml += "</ul>";
            document.getElementById("results").innerHTML = resultsHtml;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("There was an error processing your request.");
    });
