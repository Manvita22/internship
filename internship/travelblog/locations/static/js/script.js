// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('location-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Get form data
        const name = document.getElementById('location-name').value;
        const description = document.getElementById('location-description').value;
        const imageUrl = document.getElementById('location-image').value;

        // Send AJAX request to add location
        fetch('/add-location/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: `name=${name}&description=${description}&image_url=${imageUrl}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('status-message').textContent = 'Error adding location.';
            } else {
                document.getElementById('status-message').textContent = 'Location added successfully!';
                // Update the page with the new location
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('status-message').textContent = 'Error adding location.';
        });

        // Clear form
        form.reset();
    });
});
