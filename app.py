# import flask
from flask import Flask, jsonify

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

# creating our own API to display data on the specific route/URL/End point/API
@app.route("/api/v1/student/data", methods = ["GET"])
# This will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # transforms data into Json
    # Utilise Extract Transfrom Load



if __name__ == "__main__":
    app.run(debug=True)