#!/usr/bin/env python3
"""Session authentication
"""
from .auth import Auth
from typing import List
import uuid


class SessionAuth(Auth):
    """session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """"create a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        # Generate a session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the user_id in the dictionary using the session ID as the Key
        self.user_id_by_session_id[session_id] = user_id
        return session_id
