#!/usr/bin/env python3
"""Flask app
"""

from flask import Flask, request, jsonify
from auth import Auth
from typing import Tuple


# Create a Flask app
app = Flask(__name__)

# Instantiate Auth object
AUTH = Auth()


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """
    Register a user.

    Registers a new user with the provided email and password. If the user
    is already registered, returns a 400 status code with an error message.

    Args:
        None (data received via request form)

    Returns:
        tuple: A JSON response and HTTP status code.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        response = {"email": user.email, "message": "user created"}
        status_code = 200
    except ValueError:
        response = {"message": "email already registered"}
        status_code = 400

    return jsonify(response), status_code

@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Return:
        - The account login payload.
    """
    email, password = request.form.get("email"), request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
