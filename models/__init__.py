#!/usr/bin/env python3
"""
Script to initialize a FileStorage instance and reload stored data.
"""
from models.engine.file_storage import FileStorage


classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}
storage = FileStorage()
storage.reload()
