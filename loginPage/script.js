// Login form functionality
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    // Handle form submission
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const email = emailInput.value;
        const password = passwordInput.value;
        
        // Basic validation
        if (!email || !password) {
            alert('Please fill in all fields');
            return;
        }
        
        // Here you would typically send the data to a server
        console.log('Login attempt:', { email, password });
        alert('Login functionality would be implemented here');
    });

    // Input validation feedback
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    emailInput.addEventListener('blur', function() {
        if (this.value && !validateEmail(this.value)) {
            this.style.borderColor = '#e74c3c';
        } else {
            this.style.borderColor = '#ddd';
        }
    });

    emailInput.addEventListener('focus', function() {
        this.style.borderColor = '#764ba2';
    });

    passwordInput.addEventListener('focus', function() {
        this.style.borderColor = '#764ba2';
    });
});