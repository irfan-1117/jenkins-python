from flask import Flask, jsonify, render_template
from flask_wtf.csrf import CSRFProtect
import socket

app = Flask(__name__)

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Function to fetch hostname and IP address
def fetchdetails():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return str(hostname), str(ip_address)
    except socket.error:
        return "Unknown", "Unknown"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
@csrf.exempt  # Disable CSRF protection on this route
def health():
    return jsonify(status="up")

@app.route("/details")
def details():
    hostname, ip_address = fetchdetails()
    return render_template("index.html", HOSTNAME=hostname, IP=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
