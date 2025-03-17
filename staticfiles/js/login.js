// Get the login URL from the hidden input field
const loginUrl = document.getElementById('loginUrl').value;

// JavaScript to show login-div
function showLoginDiv() {
    document.getElementById('login-div').style.display = 'block';
}

// JavaScript to hide login-div
function hideLoginDiv() {
    document.getElementById('login-div').style.display = 'none';
}

//post login request with ajax
document.getElementById('loginForm').onsubmit = function(event) {
    event.preventDefault();  // Prevent default form submission

    // Submit the form via JavaScript
    const formData = new FormData(this);
    fetch(loginUrl, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',  // Identify as AJAX request
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload();  // Reload the page on successful login
        } else {
            document.getElementById('errorMessage').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
};