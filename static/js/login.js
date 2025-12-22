// Login form functionality
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    // Handle form submission
    loginForm.addEventListener('submit', function(e) {
        // Let the form submit normally to Flask backend
        const username = usernameInput.value;
        const password = passwordInput.value;
        
        // Basic validation
        if (!username || !password) {
            e.preventDefault();
            alert('Please fill in all fields');
            return;
        }
        
        // Form will submit to Flask backend for database authentication
        console.log('Login attempt for username:', username);
    });

    // Input focus effects
    usernameInput.addEventListener('focus', function() {
        this.style.borderColor = '#764ba2';
    });

    usernameInput.addEventListener('blur', function() {
        this.style.borderColor = '#ddd';
    });

    passwordInput.addEventListener('focus', function() {
        this.style.borderColor = '#764ba2';
    });

    passwordInput.addEventListener('blur', function() {
        this.style.borderColor = '#ddd';
    });
});