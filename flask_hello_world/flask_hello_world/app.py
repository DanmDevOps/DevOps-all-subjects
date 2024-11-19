from flask import Flask

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Hello, World!"

# Greeting Route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# About Route (Bonus Task)
@app.route('/about')
def about():
    return "This is a simple Flask web application that demonstrates basic routing."

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
