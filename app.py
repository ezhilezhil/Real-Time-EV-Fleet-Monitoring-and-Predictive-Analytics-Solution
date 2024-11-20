from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/histogram.html")
def histogram():
    return render_template("histogram.html")

# Add routes for other pages as needed
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

@app.route("/vehicle_Registration.html")
def vehicle_registration():
    return render_template("vehicle_registration.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
