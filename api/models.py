"""Module for representing the video game database model"""
from flask_sqlalchemy import SQLAlchemy
from typing import Optional

db = SQLAlchemy()

class VideoGame(db.Model):
    """Class that represents a video game."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False) # the property doesn't accept null as a value
    platform: str = db.Column(db.String(80), nullable=False)
    score: int = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<VideoGame {self.name}>'
