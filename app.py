from flask import Flask, render_template, jsonify, request
from datetime import datetime
import requests
from insert_data import insert_vehicle
from retrieve_data import fetch_all_vehicles
import random
from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/register_vehicle', methods=['POST'])
def register_vehicle():
    data = request.json
    print(data)
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

# Define the battery status prediction function
def predict_battery_status():
    battery_status_map = {0: "Excellent", 1: "Fair", 2: "Good", 3: "Needs Replacement"}
    # Generate a random prediction
    prediction_key = random.randint(0, 3)
    return battery_status_map[prediction_key]

@app.route('/')
def home():
    return render_template("predict_battery.html")

@app.route('/battery_health_status', methods=["POST"])
def battery_health_status():
    # Get input data from form (not actually used here since prediction is random)
    capacity = request.form["capacity"]
    cycle_count = request.form["cycle_count"]
    voltage = request.form["voltage"]
    temperature = request.form["temperature"]
    internal_resistance = request.form["internal_resistance"]

    # Generate random prediction
    prediction = predict_battery_status()

    return render_template(
        "predict_battery.html",
        prediction=prediction,
        input_data={
            "capacity": capacity,
            "cycle_count": cycle_count,
            "voltage": voltage,
            "temperature": temperature,
            "internal_resistance": internal_resistance,
        },
    )

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
