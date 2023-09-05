#!/usr/bin/env python3
"""Authorize authentication
"""

from typing import List, TypeVar
from flask import request


class Auth:
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
