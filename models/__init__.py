#!/usr/bin/env python3
"""
Script to initialize a FileStorage instance and reload stored data.
"""
from models.engine.file_storage import FileStorage

"fileStorage operations"
storage = FileStorage()
storage.reload()
