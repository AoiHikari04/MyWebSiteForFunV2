# Flask App Runner
from app import app

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open your browser and navigate to: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='127.0.0.1', port=5000)