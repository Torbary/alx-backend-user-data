#!/usr/bin/env pyhton3
"""Authorize authentication
"""


from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """placeholder method for authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Placeholder method for getting the authorization headerself.
        """
        return None

    def current_user(self, request=None):
        """placeholder method for getting the current user"""
        return None
