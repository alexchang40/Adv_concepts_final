function submitForm() {
    const sequence = document.getElementById('sequence').value.trim();

    if (!sequence) {
        alert('Please enter a sequence!');
        return;
    }

    // Create a FormData object to send the sequence
    const formData = new FormData();
    formData.append('sequence', sequence);

    // Send a POST request to the CGI script
    fetch('/cgi-bin/peptide_analysis.py', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let resultsHtml = '<h2>Results:</h2><ul>';
            for (const aa in data) {
                resultsHtml += `<li>${aa}: ${data[aa]}</li>`;
            }
            resultsHtml += '</ul>';
            document.getElementById('results').innerHTML = resultsHtml;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error processing your request.');
    });
