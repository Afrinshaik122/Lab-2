from flask import Flask, render_template
from models import fetch_data
from views import render_data

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Fetch data from the model
        data = fetch_data()
        # Render data using the view
        return render_data(data)
    except Exception as e:
        # Handle errors and return an appropriate response
        return f"An error occurred: {e}", 500

# Ensure the app runs only when executed directly
if __name__ == '__main__':
    app.run(debug=True)
