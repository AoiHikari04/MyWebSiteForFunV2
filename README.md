dw# AI Tool Portal - Flask Web Application

A simple Flask web application for managing AI tools with a modern, responsive design.

## Project Structure

```
MyWebSiteForFunV2/
├── app.py              # Main Flask application
├── run.py              # Application runner
├── config.py           # Configuration settings
├── database.py         # SQLite database functions and initialization
├── users.db            # SQLite database file (created automatically)
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html       # Base templatev
│   ├── index.html      # Homepage
│   ├── login.html      # Login page
│   └── profile.html    # Profile settings page
├── static/             # Static files
│   ├── css/
│   │   ├── styles.css  # Main styles
│   │   └── login.css   # Login page styles
│   └── js/
│       ├── script.js   # Main JavaScript
│       └── login.js    # Login page JavaScript
├── homepage/           # Original static files (legacy)
└── loginPage/          # Original static files (legacy)
```

## Features

- **Protected Homepage**: AI tool dashboard requires authentication to access
- **Database Authentication**: SQLite database with secure password hashing (SHA-256)
- **Session Management**: Proper login/logout functionality with session tracking
- **Profile Settings**: User profile management with password change functionality
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Glassmorphism effects and smooth transitions
- **Security**: Passwords stored as SHA-256 hashes, never in plain text

## Installation

1. **Clone/Navigate to the project directory**
   ```bash
   cd MyWebSiteForFunV2
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Method 1: Using run.py (Recommended)
```bash
python run.py
```

### Method 2: Using Flask directly
```bash
python app.py
```

### Method 3: Using Flask CLI
```bash
flask run
```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. **You'll be automatically redirected to the login page** (homepage is protected)
3. Use the database credentials to log in:
   - **Username**: admin
   - **Password**: admin
4. After successful login, you'll be redirected to the **Command Center** (homepage)
5. Use the navigation buttons to switch between **Home** and **Profile Settings**
6. In **Profile Settings**, you can view your account info and change your password
7. Click **Logout** when you're done to end your session

## API Endpoints

- `GET /` - Protected Homepage (redirects to login if not authenticated)
- `GET /login` - Login page (entry point for unauthenticated users)
- `POST /login` - Process login form
- `GET /logout` - Logout and clear session
- `GET /profile` - Profile settings page with account information
- `POST /profile` - Process password change requests
- `GET /api/tools` - Protected JSON API for tools data

## Development

- The application runs in debug mode by default
- Changes to Python files will automatically reload the server
- Static files (CSS/JS) changes require a browser refresh

## Customization

- **Styles**: Edit files in `static/css/`
- **JavaScript**: Edit files in `static/js/`
- **Templates**: Edit files in `templates/`
- **Configuration**: Edit `config.py`

## Authentication

The application now uses SQLite database for secure user authentication:

### Database Features:
- **SQLite Database**: Lightweight, serverless database stored in `users.db`
- **Secure Passwords**: All passwords are hashed using SHA-256 before storage
- **Admin Account**: Pre-created admin user with username `admin` and password `admin`
- **Session Management**: Flask sessions track user authentication state

### Default Credentials:
- **Username**: `admin`
- **Password**: `admin` (stored as SHA-256 hash in database)

### Security Implementation:
- Passwords are never stored in plain text
- SHA-256 hashing for password security
- Session-based authentication
- Protected routes with login decorators

### Database Schema:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS, Custom CSS
- **Icons**: Font Awesome
- **Template Engine**: Jinja2 (included with Flask)