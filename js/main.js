function analyzePeptide() {
    const sequence = document.getElementById('sequence').value.trim();
    
    if (sequence === '') {
        alert('Please enter a sequence!');
        return;
    }

    // Example: Count amino acids (simple example, you should extend it)
    const aaCounts = {};
    for (let i = 0; i < sequence.length; i++) {
        const aa = sequence[i].toUpperCase();
        if (aaCounts[aa]) {
            aaCounts[aa]++;
        } else {
            aaCounts[aa] = 1;
        }
    }

    // Display results
    let resultsHtml = '<h2>Results:</h2>';
    resultsHtml += '<ul>';
    for (const aa in aaCounts) {
        resultsHtml += `<li>${aa}: ${aaCounts[aa]}</li>`;
    }
    resultsHtml += '</ul>';

    document.getElementById('results').innerHTML = resultsHtml;
}
