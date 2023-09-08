#!/usr/bin/env python3
"""Session authentication module for the API
"""
import os
from flask import request, jsonify, abort
from models.user import User
from api.v1.views import app_views


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_auth_login():
    """session authentication login route
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return response, 200