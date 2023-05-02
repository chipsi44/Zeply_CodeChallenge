from flask import Flask, render_template, request
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route("/", methods=["GET", "POST"])
def predict():
    # Check the request method
    if request.method == "GET":
        # If the request method is GET, return the index.html template
        print("ALIVE")
        return render_template("index.html")
    else:  
        return render_template("index.html")

# Start the Flask app
app.run(debug=False)