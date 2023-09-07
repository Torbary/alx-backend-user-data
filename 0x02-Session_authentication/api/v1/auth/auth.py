#!/usr/bin/env python3
"""Authorize authentication
"""

from typing import List, TypeVar
from flask import request
import os

class Auth:
    """Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Placeholder method for authentication requirement.

        Args:
            path (str): The path being accessed.
            excluded_paths (list): List of paths to be excluded from
            authentication.

        Returns:
            bool: Always returns False (authentication not implemented yet).
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method for getting the authorization header.

        Args:
            request (Flask request): The Flask request object.

        Returns:
            str: Always returns None (authorization not implemented yet).
        """
        if request is not None:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for getting the current user.

        Args:
            request (Flask request): The Flask request object.

        Returns:
            TypeVar('User'): Always returns None (user not implemented yet).
        """
        return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.

        Args:
            path (str): The path being accessed.
            excluded_paths (List[str]): List of paths to be excluded from
            authentication.

        Returns:
            bool: True if authentication is required, False if not.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize paths to ensure trailing slash consistency
        normalized_path = path.rstrip("/") + "/"

        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                excluded_path = excluded_path.rstrip("/") + "/"

            if normalized_path.startswith(excluded_path):
                return False

        return True

    def session_cookie(self, request=None) -> str:
        """Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
