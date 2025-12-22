from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from functools import wraps
from database import init_database, get_user_by_username, verify_password, update_user_password

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize database on startup
init_database()

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route for the main dashboard (homepage) - now protected
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Route for the login page (now the default public page)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect to homepage
    if 'logged_in' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Database authentication
        user = get_user_by_username(username)
        
        if user and verify_password(password, user[2]):  # user[2] is password_hash column
            session['logged_in'] = True
            session['user_id'] = user[0]  # user[0] is id column
            session['username'] = user[1]  # user[1] is username column
            session['user_email'] = user[3] if user[3] else f"{username}@example.com"  # user[3] is email column
            flash(f'Welcome back, {username}! Login successful.', 'success')
            return redirect(url_for('index'))  # Redirect to homepage after login
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

# Route for logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('login'))

# Route for the profile settings (replaces dashboard)
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    username = session.get('username', 'Unknown User')
    user_email = session.get('user_email', 'Unknown Email')
    user_id = session.get('user_id')
    
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password != confirm_password:
            flash('New passwords do not match', 'error')
        elif len(new_password) < 3:  # Basic password validation
            flash('New password must be at least 3 characters long', 'error')
        else:
            # Update password in database
            if update_user_password(user_id, new_password):
                flash('Password updated successfully!', 'success')
            else:
                flash('Failed to update password', 'error')
    
    return render_template('profile.html', username=username, user_email=user_email)

# API route for tool cards data - now protected
@app.route('/api/tools')
@login_required
def get_tools():
    tools = [
        {"id": "n8n", "name": "n8n Workflow Automation", "url": "https://n8n.aoihikari.my"},
        {"id": "a1111", "name": "Automatic1111", "url": "https://a1111.example.com", "outputsUrl": "https://a1111.example.com/outputs"},
        {"id": "video", "name": "Video Generation", "url": "https://runwayml.com"}
    ]
    return tools

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)