#!/usr/bin/env python3
"""Session authentication
"""
from .auth import Auth
from typing import List
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get USER ID bases on a Session ID"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """return a user instnace based on a cookie value (overload)"""
        if request:
            session_cookie = self.session_cookie(request)
            if session_cookie:
                user_id = self.user_id_for_session_id(session_cookie)
                if user_id:
                    user = User.get(user_id)
                    return user
        return None
