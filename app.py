from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import pickle
import numpy as np
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

# ===============================
# Database connection
# ===============================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ===============================
# Load ML files
# ===============================
model = pickle.load(open("rf_risk_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# ===============================
# LOGIN
# ===============================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = user["email"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

# ===============================
# REGISTER
# ===============================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (email, password) VALUES (?,?)",
                (email, password)
            )
            conn.commit()
        except:
            conn.close()
            return render_template("register.html", error="User already exists")

        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")

# ===============================
# LOGOUT
# ===============================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ===============================
# HOME / PREDICTION
# ===============================
@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    prediction = None
    advice = ""
    next_period = ""

    if request.method == "POST":
        try:
            features = [
                int(request.form["age"]),
                int(request.form["cycle_length"]),
                int(request.form["period_duration"]),
                int(request.form["flow_level"]),
                int(request.form["cramps"]),
                int(request.form["mood_swings"]),
                int(request.form["acne"]),
                int(request.form["weight_gain"]),
                int(request.form["hair_fall"]),
                int(request.form["fatigue"]),
                int(request.form["irregular_periods"]),
                int(request.form["missed_periods"]),
            ]

            features = scaler.transform(np.array(features).reshape(1, -1))
            pred = model.predict(features)[0]
            prediction = label_encoder.inverse_transform([pred])[0]

            advice_map = {
                "Normal": "Your cycle appears normal. Maintain a healthy lifestyle.",
                "PCOS": "Consult a gynecologist for PCOS management.",
                "Hormonal Imbalance": "Monitor hormonal levels and manage stress.",
                "High Risk": "Seek medical attention immediately."
            }
            advice = advice_map[prediction]

            last_date = request.form.get("last_period_date")
            if last_date:
                last_date = datetime.strptime(last_date, "%Y-%m-%d")
                next_period = (
                    last_date + timedelta(days=int(request.form["cycle_length"]))
                ).strftime("%Y-%m-%d")

        except Exception as e:
            advice = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        advice=advice,
        next_period=next_period
    )

if __name__ == "__main__":
    app.run(debug=True)
