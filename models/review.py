#!/usr/bin/env python3
"""
Module of the class Reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): string
    """

    place_id = ""
    user_id = ""
    text = ""
