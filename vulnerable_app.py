#!/usr/bin/env python3
"""
vulnerable_app.py
Personal Cybersecurity Project - Secure Coding Review
Target Application (Intentionally Vulnerable Flask App)
Author: Adithyan V

WARNING: This app is intentionally vulnerable for educational purposes.
DO NOT deploy this in production.
"""

from flask import Flask, request, render_template_string
import sqlite3
import subprocess
import hashlib
import os

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded secret key
app.secret_key = "supersecretkey123"

# VULNERABILITY 2: Hardcoded credentials
DB_USER = "admin"
DB_PASS = "admin123"

# ─── Database Setup ───────────────────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)""")
    # VULNERABILITY 3: Passwords stored as plain MD5 (weak hashing)
    c.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', ?)",
              (hashlib.md5(b"admin123").hexdigest(),))
    conn.commit()
    conn.close()

# ─── Routes ──────────────────────────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # VULNERABILITY 4: SQL Injection — user input directly in query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        user = c.fetchone()
        conn.close()

        if user:
            return f"Welcome {username}!"
        else:
            error = "Invalid credentials"

    # VULNERABILITY 5: XSS — user input reflected without sanitization
    return render_template_string(f"""
        <h2>Login</h2>
        <form method='post'>
            Username: <input name='username'><br>
            Password: <input name='password' type='password'><br>
            <input type='submit' value='Login'>
        </form>
        <p style='color:red'>{error}</p>
    """)


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")

    # VULNERABILITY 6: Command Injection — user input passed to shell
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result.decode()


@app.route("/file")
def read_file():
    filename = request.args.get("name", "readme.txt")

    # VULNERABILITY 7: Path Traversal — no path sanitization
    with open(f"/var/www/files/{filename}", "r") as f:
        return f.read()


@app.route("/debug")
def debug():
    # VULNERABILITY 8: Debug mode exposes stack traces and internal info
    raise Exception("Debug endpoint — exposing internal error info!")


if __name__ == "__main__":
    init_db()
    # VULNERABILITY 9: Debug=True in production exposes Werkzeug debugger
    app.run(debug=True, host="0.0.0.0", port=5000)
