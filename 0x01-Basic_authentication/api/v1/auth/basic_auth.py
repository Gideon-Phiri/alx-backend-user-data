#!/usr/bin/env python3
"""
BasicAuth class that inherits from Auth
"""
from models.user import User
import base64
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    pass


def extract_base64_authorization_header(self, authorization_header: str) -> str:
    if authorization_header is None or not isinstance(authorization_header, str):
        return None
    if not authorization_header.startswith("Basic "):
        return None
    return authorization_header[6:]  # Extracts part after 'Basic '


def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
    if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
        return None
    try:
        decoded = base64.b64decode(base64_authorization_header).decode('utf-8')
    except Exception:
        return None
    return decoded


def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
    if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
        return None, None
    if ':' not in decoded_base64_authorization_header:
        return None, None
    return tuple(decoded_base64_authorization_header.split(':', 1))  # Split into user and password


def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
    if user_email is None or not isinstance(user_email, str):
        return None
    if user_pwd is None or not isinstance(user_pwd, str):
        return None
    user = User.search({"email": user_email})
    if not user or not user[0].is_valid_password(user_pwd):
        return None
    return user[0]


def current_user(self, request=None) -> TypeVar('User'):
    auth_header = self.authorization_header(request)
    if auth_header is None:
        return None
    base64_auth = self.extract_base64_authorization_header(auth_header)
    if base64_auth is None:
        return None
    decoded_auth = self.decode_base64_authorization_header(base64_auth)
    if decoded_auth is None:
        return None
    email, password = self.extract_user_credentials(decoded_auth)
    if email is None or password is None:
        return None
    return self.user_object_from_credentials(email, password)


def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
    """
    Extracts the user email and password from the Base64 decoded string.
    The string will be of the form "email:password", but the password
    can contain colons as well.
    """
    if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
        return None, None
    
    # Split once on the first colon
    try:
        email, password = decoded_base64_authorization_header.split(':', 1)
    except ValueError:
        return None, None
    
    return email, password
