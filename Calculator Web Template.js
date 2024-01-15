// Function to solve the current math problem in the input field
function solve() {
    // Try to evaluate the current input as a math expression
    try {
        var result = eval(document.getElementById('result').value);
 
        // Use AJAX to send the result to the Flask backend
        fetch('/calculate', {
            // Specify the method as POST
            method: 'POST',
            // Set the content type to JSON
            headers: {
                'Content-Type': 'application/json'
            },
            // Send the result as JSON in the request body
            body: JSON.stringify({ result: result })
        })
        // Parse the response as JSON
        .then(response => response.json())
        // Update the input field with the calculated result from the server
        .then(data => {
            document.getElementById('result').value = data.result;
        })
        // Log any errors to the console
        .catch(error => console.error('Error:', error));
 
    // If there was an error evaluating the input, display "Error" in the input field
    } catch (error) {
        document.getElementById('result').value = 'Error';
    }
 }
 
 // Function to clear the input field
 function clear() {
    document.getElementById('result').value = '';
 }