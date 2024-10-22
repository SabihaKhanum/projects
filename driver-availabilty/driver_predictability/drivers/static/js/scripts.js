document.getElementById('distanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const destination = document.getElementById('destination').value;
    const resultDiv = document.getElementById('result');

    // Assuming you have an endpoint like /api/get_distance
    fetch(`/api/get_distance?destination=${encodeURIComponent(destination)}`)
        .then(response => response.json())
        .then(data => {
            if (data.distance) {
                resultDiv.innerHTML = `Distance to ${destination}: ${data.distance} km`;
            } else {
                resultDiv.innerHTML = `Error: ${data.message}`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `Error: ${error.message}`;
        });
});