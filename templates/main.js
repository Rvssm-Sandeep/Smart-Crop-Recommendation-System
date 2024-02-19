document.getElementById('cropForm').addEventListener('submit', function (event) {
    // Client-side validation
    var stateName = document.getElementById('stateName').value;
    var cropType = document.getElementById('cropType').value;
    var rainfall = document.getElementById('rainfall').value;
    var temperature = document.getElementById('temperature').value;
    var nitrogen = document.getElementById('nitrogen').value;
    var phosphorous = document.getElementById('phosphorous').value;
    var potassium = document.getElementById('potassium').value;

    // Check if any of the required fields are empty
    if (!stateName || !cropType || !rainfall || !temperature || !nitrogen || !phosphorous || !potassium) {
        alert('Please fill in all fields.');
        event.preventDefault();
        return;
    }

    // Additional client-side validation logic can be added as needed

    // Redirect to the output page after successful validation
    window.location.href = 'output.html';

    // Prevent the form from submitting (comment this line if you want the form to submit normally)
    event.preventDefault();
});

// Placeholder function for handling data on the output page
function handleOutputData() {
    // Retrieve data from sessionStorage (replace this with actual data retrieval logic)
    var recommendations = JSON.parse(sessionStorage.getItem('cropRecommendations'));

    // Example: Display data in the console
    console.log('Recommended Crop:', recommendations.recommendedCrop);
    console.log('Details:', recommendations.details);

    // Add your logic to display data on the output page
}
