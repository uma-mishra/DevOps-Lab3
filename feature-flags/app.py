from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Feature flags
FEATURE_FLAGS = {
    "new_dashboard": True,
    "dark_mode": False,
    "beta_feature": False
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Feature Flag Demo</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            padding: 40px;
        }
        .container {
            background: white;
            padding: 25px;
            border-radius: 10px;
            max-width: 550px;
            margin: auto;
        }
        .enabled { color: green; }
        .disabled { color: red; }
    </style>
</head>
<body>
<div class="container">
    <h1>Feature Flag Dashboard</h1>
    {% for name, enabled in flags.items() %}
        <p>
            <strong>{{ name }}</strong>:
            <span class="{{ 'enabled' if enabled else 'disabled' }}">
                {{ 'ENABLED' if enabled else 'DISABLED' }}
            </span>
        </p>
    {% endfor %}
    <p>Feature flags control which application features are available.</p>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, flags=FEATURE_FLAGS)

@app.route("/api/flags")
def get_flags():
    return jsonify(FEATURE_FLAGS)

@app.route("/api/flags/<name>/<status>", methods=["POST"])
def update_flag(name, status):
    if name not in FEATURE_FLAGS:
        return jsonify({"error": "Unknown feature flag"}), 404

    if status not in ["on", "off"]:
        return jsonify({"error": "Status must be on or off"}), 400

    FEATURE_FLAGS[name] = (status == "on")
    return jsonify({"feature": name, "enabled": FEATURE_FLAGS[name]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
