# import flask
from flask import Flask, jsonify, redirect, url_for

# create an instance of our app
app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Sam", "last_name": "Turton", "Course": "DevOps"}
    ]

# decorator - to create our api/url for user to access our data in the browser
@app.route("/") # localhost:5000 is default port for Flask
def home():
    return "This is a dream team of DevOps consultants celebrating a WOW moment!!"
# This function runs when the URL/API is accessed

@app.route("/welcome/")
def greet_user():
    return "Welcome to DevOps team"

# creating our own API to display data on the specific route/URL/End point/API
@app.route("/api/v1/student/data/", methods = ["GET"])
# This will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # transforms data into Json
    # Utilise Extract Transfrom Load


#  Find out the module to redirect the user back to specific page (welcome page)
@app.route("/login/")
def login():
    return redirect(url_for("greet_user")) # will redirect to greet user function and run it

# If page is not found (status code 404) redirect the user to welcome page
@app.errorhandler(Exception)
def handle_not_found(error):
    return redirect(url_for("welcome_screen"))

# Creates a page for if the user puts any username in the url
@app.route("/user/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps dear {username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)