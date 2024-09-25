#!/usr/bin/env python3
import requests


BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """Test registering a new user."""
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/users", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test logging in with an incorrect password."""
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test logging in with the correct password."""
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert response.status_code == 200
    assert "session_id" in response.cookies
    return response.cookies["session_id"]


def profile_unlogged() -> None:
    """Test accessing profile when not logged in."""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test accessing profile when logged in."""
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """Test logging out of the session."""
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Test generating a reset password token."""
    payload = {"email": email}
    response = requests.post(f"{BASE_URL}/reset_password", data=payload)
    assert response.status_code == 200
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test updating the password."""
    payload = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(f"{BASE_URL}/reset_password", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
