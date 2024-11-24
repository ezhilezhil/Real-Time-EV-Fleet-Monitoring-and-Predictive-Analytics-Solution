from flask import Flask, render_template
from flask_pymongo import PyMongo
import requests
from datetime import datetime

app = Flask(__name__)

# Your MongoDB URI - replace it with your own MongoDB URI (localhost:27017)
app.config["MONGO_URI"] = "mongodb://localhost:27017/vehicleDB"  # Connect to 'vehicleDB' database
mongo = PyMongo(app)

# Your OpenWeather API key (replace with your own API key)
API_KEY = '269cd9d63b71b57a3134fbe597aceb8b'
CITY = 'India'  # Replace with the city for which you want the weather data

# OpenWeather API URL
BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'


@app.route("/")
def index():
    return render_template("index.html")


# Login page route
@app.route("/login.html")
def login():
    return render_template("login.html")

# Register page route
@app.route("/register.html")
def register():
    return render_template("register.html")

# Forgot Password page route
@app.route("/forgot_password.html")
def forgot_password():
    return render_template("forgot_password.html")

# Battery Health Status Section route
@app.route("/Battery Health Status Section.html")
def Battery_Health_Status_Section():
    return render_template("Battery Health Status Section.html")

# Cost and Energy Consumption page route
@app.route("/Cost and Energy Consumption.html")
def Cost_and_Energy_Consumption():
    return render_template("Cost and Energy Consumption.html")

# Display Behavior Analysis and Alerts page route
@app.route("/Display Behavior Analysis and Alerts.html")
def Display_Behavior_Analysis_and_Alerts():
    return render_template("Display Behavior Analysis and Alerts.html")

# Driver Behavior and Maintenance Alerts page route
@app.route("/Driver Behavior and Maintenance Alerts.html")
def Driver_Behavior_and_Maintenance_Alerts():
    return render_template("Driver Behavior and Maintenance Alerts.html")

# Report Generation page route
@app.route("/Report Generation.html")
def Report_Generation():
    return render_template("Report Generation.html")

# Vehicle Registration page route
@app.route("/vehicle_Registration.html")
def vehicle_registration():
    return render_template("vehicle_registration.html")


# Histogram page route
@app.route("/histogram.html")
def histogram():
    return render_template("histogram.html")

# Other routes remain the same...

if __name__ == "__main__":
    # Run the app with debugging enabled
    app.run(host="0.0.0.0", port=5001, debug=True)
