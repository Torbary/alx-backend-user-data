#!/usr/bin/env python3
"""
Module: user.py
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for the 'users' table.
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: str = None, reset_token: str = None):
        """
        Initialize a User object.

        Args:
            email (str): User's email address.
            hashed_password (str): Hashed password for the user.
            session_id (str, optional): Session ID for the user.
                Defaults to None.
            reset_token (str, optional): Reset token for the user.
                Defaults to None.
        """
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token


# Ensure the file is executable
if __name__ == "__main__":
    pass
