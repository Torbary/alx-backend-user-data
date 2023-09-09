#!/usr/bin/env python3
"""User session"""

from typing import Dict, List
from models.base import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class UserSession(Base):
    """UserSession model for storing session data in the database"""
    __tablename__ = "user_sessions"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    session_id = Column(String(60), nullable=False)

    user = relationship("User")

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        """Initializes UserSession"""
        super().__init__(*args, **kwargs)
