#!/usr/bin/env python3
"""
Auth class to manage authentication
"""
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: list) -> bool:
    if path is None or excluded_paths is None or len(excluded_paths) == 0:
        return True
    if path[-1] != '/':
        path += '/'
    return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
    if request is None or 'Authorization' not in request.headers:
        return None
    return request.headers.get('Authorization')

    def current_user(self, request=None):
        return None

def require_auth(self, path: str, excluded_paths: list) -> bool:
    """
    Returns True if the requested path requires authentication, False if it's
    in the excluded paths. Supports wildcards at the end of the excluded paths.
    """
    if path is None:
        return True
    if excluded_paths is None or len(excluded_paths) == 0:
        return True
    
    # Add a trailing slash if missing
    if not path.endswith('/'):
        path += '/'

    # Check against each path in excluded_paths
    for excluded_path in excluded_paths:
        # Handle wildcard paths ending with '*'
        if excluded_path.endswith('*'):
            if path.startswith(excluded_path[:-1]):
                return False
        elif path == excluded_path:
            return False

    return True
