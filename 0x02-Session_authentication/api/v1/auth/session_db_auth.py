#!/usr/bin/env python3
"""Session auth wtih DB storage"""

from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Session authentication with database storage."""

    def create_session(self, user_id=None) -> str:
        """Create a Session ID and store it in the database."""
        session_id = super().create_session(user_id)
        if type(session_id) == str:
            kwargs = {
                "user_id": user_id,
                "session_id": session_id,
            }
            new_session = UserSession(**kwargs)
            new_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve a User ID from the database based on Session ID."""
        if not session_id:
            return None
        user_session = UserSession.search({'session_id': session_id})
        if user_session:
            return user_session[0].user_id
        return None

    def destroy_session(self, request=None) -> bool:
        """Destroy the UserSession from the database based on Session ID."""
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_sessions = UserSession.search({'session_id': session_id})
                if user_sessions:
                    user_sessions[0].remove()
                    return True
        return False
