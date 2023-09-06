#!/usr/bin/env python3
"""Basic authentication module for the API
"""
from typing import Tuple, TypeVar
from .auth import Auth
import re
import base64


class BasicAuth(Auth):
    """Basic authentication class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:

        """Returns the Base64 part of the Authorization
            header for a Basic Authentication:
        """
        if type(authorization_header) == str:
            pattern = r"Basic (?P<token>.+)"
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group("token")
            return None
