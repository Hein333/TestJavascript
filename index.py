import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")


# API endpoint that provides fresh data as JSON
@app.route("/api/data")
def get_data():
    # Simulated dynamic data (replace with a database query, pandas DataFrame, etc.)
    data = [
        {
            "id": 1,
            "server": "Alpha",
            "cpu": f"{random.randint(10, 95)}%",
            "status": "Online",
        },
        {
            "id": 2,
            "server": "Beta",
            "cpu": f"{random.randint(10, 95)}%",
            "status": "Online",
        },
        {
            "id": 3,
            "server": "Gamma",
            "cpu": f"{random.randint(10, 95)}%",
            "status": "Maintenance",
        },
        {
            "id": 4,
            "server": "Apple",
            "cpu": f"{random.randint(10, 95)}%",
            "status": "Maintenance",
        },
    ]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
