#!/usr/bin/env python3
"""
Main file
"""

import bcrypt
from sqlalchemy import False_  # Import bcrypt library
from db import DB, NoResultFound, except_
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If a user with the same email already exists.
        """
        # Check if a user with the provided email already exists
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """checks if a user's login details are valid"""
        try:
            user = self._db.find_user_by(email=email)
            # Compare the provided password with the hasshed password in the db
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False
