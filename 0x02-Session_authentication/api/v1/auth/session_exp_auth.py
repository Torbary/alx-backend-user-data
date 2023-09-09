#!/usr/bin/env python3
"""Session ID expiration date"""

import os
from os import getenv
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """add an expiration date to a Session ID
    """
    def __init__(self) -> None:
        """instantiate the class SessionExpAuth
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION", 0))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session ID with expiration date"""
        session_id = super().create_session(user_id)
        if session_id:
            session_dict = {
                "user_id": user_id,
                "created_at": datetime.now()
            }
            self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves the user id of the user associated with
        a given session id.
        """
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' not in session_dict:
                return None
            cur_time = datetime.now()
            time_span = timedelta(seconds=self.session_duration)
            exp_time = session_dict['created_at'] + time_span
            if exp_time < cur_time:
                return None
            return session_dict['user_id']
