#!/usr/bin/env python3
"""
encrypt_password module handles password hashing and validation using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
    - password: The password to be hashed.

    Returns:
    - Salted, hashed password as bytes
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against its hashed version.

    Args:
    - hashed_password: The hashed password as bytes
    - password: The plain-text password to validate

    Returns:
    - True if the password matches the hash, False otherwise
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
