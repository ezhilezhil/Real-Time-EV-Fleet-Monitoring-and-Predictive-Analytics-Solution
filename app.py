from flask import Flask, render_template, request, jsonify
import pickle
import random
from datetime import datetime
import requests
from insert_data import insert_vehicle
from retrieve_data import fetch_all_vehicles
import numpy as np

app = Flask(__name__)

# Load the trained battery status prediction model
with open("battery_health_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# OpenWeather API details
API_KEY = '269cd9d63b71b57a3134fbe597aceb8b'
CITY = 'India'
BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/forgot_password.html")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/Battery Health Status Section.html")
def Battery_Health_Status_Section():
    return render_template("Battery Health Status Section.html")

@app.route("/Cost and Energy Consumption.html")
def Cost_and_Energy_Consumption():
    return render_template("Cost and Energy Consumption.html")

@app.route("/Display Behavior Analysis and Alerts.html")
def Display_Behavior_Analysis_and_Alerts():
    return render_template("Display Behavior Analysis and Alerts.html")

@app.route("/Driver Behavior and Maintenance Alerts.html")
def Driver_Behavior_and_Maintenance_Alerts():
    return render_template("Driver Behavior and Maintenance Alerts.html")

@app.route("/Report Generation.html")
def Report_Generation():
    return render_template("Report Generation.html")

@app.route("/vehicle_registration.html")
def vehicle_registration():
    return render_template("vehicle_registration.html")

@app.route("/histogram.html")
def histogram():
    return render_template("histogram.html")

@app.route('/register_vehicle', methods=['POST'])
def register_vehicle():
    data = request.json
    try:
        insert_vehicle(
            data['vehicle_name'],
            data['vehicle_model'],
            data['registration_number'],
            data['battery_capacity']
        )
        return jsonify({"message": "Vehicle registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    vehicles = fetch_all_vehicles()
    return jsonify(vehicles), 200

@app.route('/battery_health_status', methods=['POST'])
def battery_health_status():
    try:
        # Get form inputs
        capacity = float(request.form['capacity'])
        cycle_count = int(request.form['cycle_count'])
        voltage = float(request.form['voltage'])
        temperature = float(request.form['temperature'])
        resistance = float(request.form['resistance'])
        
        # Create feature array for prediction
        features = np.array([[capacity, cycle_count, voltage, temperature, resistance]])
        
        # Make prediction
        prediction = model.predict(features)
        health_percentage = prediction[0]
        
        # Categorize battery health based on predicted percentage
        if health_percentage >= 90:
            health_status = "Excellent"
        elif 80 <= health_percentage < 90:
            health_status = "Good"
        elif 60 <= health_percentage < 80:
            health_status = "Fair"
        else:
            health_status = "Needs Replacement"
        
        # Return the result with the health status
        return render_template('Battery Health Status Section.html', prediction_text=f"Predicted Battery Health: {health_percentage:.2f}% - {health_status}")
    except Exception as e:
        return render_template('Battery Health Status Section.html', prediction_text=f"Error: {e}")

@app.route('/optimize_route')
def optimize_route():
    # Mock route suggestions
    route_suggestions = [
        "Route 1: Start → Charging Station A → Destination",
        "Route 2: Start → Charging Station B → Destination",
        "Route 3: Start → Charging Station C → Destination"
    ]
    return render_template('optimize_route.html', routes=route_suggestions)

if __name__ == "__main__":
    # Run the app with debugging enabled
    app.run(host="0.0.0.0", port=5001, debug=True)
