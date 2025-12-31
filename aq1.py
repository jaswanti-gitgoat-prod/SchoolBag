# vulnerable_app.py
# INTENTIONALLY VULNERABLE – FOR SAST TESTING ONLY

from flask import Flask, request
import sqlite3
import os
import pickle
import subprocess

app = Flask(__name__)

# ----------------------------
# Hardcoded secret (SAST: Hardcoded Credentials)
# ----------------------------
SECRET_KEY = "super-secret-password"

# ----------------------------
# SQL Injection
# ----------------------------
@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable: string concatenation in SQL query
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful"
    return "Login failed"

# ----------------------------
# Command Injection
# ----------------------------
@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Vulnerable: user input passed directly to shell
    os.system("ping -c 1 " + host)
    return "Ping executed"

# ----------------------------
# Cross-Site Scripting (XSS)
# ----------------------------
@app.route("/greet")
def greet():
    name = request.args.get("name")

    # Vulnerable: reflected XSS
    return "<h1>Hello " + name + "</h1>"

# ----------------------------
# Insecure Deserialization
# ----------------------------
@app.route("/load")
def load():
    data = request.args.get("data")

    # Vulnerable: untrusted deserialization
    obj = pickle.loads(data.encode())
    return str(obj)

# ----------------------------
# Path Traversal
# ----------------------------
@app.route("/read")
def read_file():
    filename = request.args.get("file")

    # Vulnerable: no path validation
    with open(filename, "r") as f:
        return f.read()

# ----------------------------
# Unsafe subprocess usage
# ----------------------------
@app.route("/run")
def run():
    cmd = request.args.get("cmd")

    # Vulnerable: command injection via subprocess
    subprocess.call(cmd, shell=True)
    return "Command executed"

if __name__ == "__main__":
    app.run(debug=True)
