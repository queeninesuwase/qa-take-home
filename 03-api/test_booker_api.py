import pytest
import requests


def test_create_auth_token(base_url):
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "token" in data
    assert isinstance(data["token"], str)
    assert data["token"] != ""


def test_invalid_auth_credentials(base_url):
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "invalid_user", "password": "invalid_password"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "reason" in data
    assert data["reason"] == "Bad credentials"


def test_create_booking(created_booking, booking_data):
    assert created_booking["booking_id"] is not None

    booking = created_booking["booking"]

    assert booking["firstname"] == booking_data["firstname"]
    assert booking["lastname"] == booking_data["lastname"]
    assert booking["totalprice"] == booking_data["totalprice"]
    assert booking["depositpaid"] == booking_data["depositpaid"]
    assert booking["bookingdates"] == booking_data["bookingdates"]


def test_get_created_booking(base_url, created_booking, booking_data):
    booking_id = created_booking["booking_id"]

    response = requests.get(f"{base_url}/booking/{booking_id}", timeout=10)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert data["firstname"] == booking_data["firstname"]
    assert data["lastname"] == booking_data["lastname"]
    assert data["totalprice"] == booking_data["totalprice"]
    assert data["depositpaid"] == booking_data["depositpaid"]


def test_update_booking_with_put(base_url, auth_token, created_booking):
    booking_id = created_booking["booking_id"]

    updated_booking = {
        "firstname": "Test",
        "lastname": "Example",
        "totalprice": 350,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-11-12", "checkout": "2026-11-18"},
        "additionalneeds": "Lunch",
    }

    response = requests.put(
        f"{base_url}/booking/{booking_id}",
        json=updated_booking,
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert data["firstname"] == "Test"
    assert data["lastname"] == "Example"
    assert data["totalprice"] == 350
    assert data["depositpaid"] is False
    assert data["bookingdates"]["checkin"] == "2026-11-12"
    assert data["bookingdates"]["checkout"] == "2026-11-18"
    assert data["additionalneeds"] == "Lunch"


def test_partial_update_booking_with_patch(base_url, auth_token, created_booking):
    booking_id = created_booking["booking_id"]

    partial_update = {"firstname": "Test", "additionalneeds": "Dinner"}

    response = requests.patch(
        f"{base_url}/booking/{booking_id}",
        json=partial_update,
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert data["firstname"] == "Test"
    assert data["additionalneeds"] == "Dinner"


def test_delete_booking(base_url, auth_token, created_booking):
    booking_id = created_booking["booking_id"]

    response = requests.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )

    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 2

    get_response = requests.get(f"{base_url}/booking/{booking_id}", timeout=10)

    assert get_response.status_code == 404


@pytest.mark.xfail(
    reason="API returns 500 instead of a client validation error for missing booking fields"
)
def test_create_booking_with_missing_fields(base_url):
    incomplete_booking = {"firstname": "Test", "lastname": "User"}

    response = requests.post(f"{base_url}/booking", json=incomplete_booking, timeout=10)

    assert response.status_code in [400, 422]
    assert response.elapsed.total_seconds() < 2
    assert response.text.strip() != ""


@pytest.mark.xfail(
    reason="API accepts incorrect data types instead of returning a validation error"
)
def test_create_booking_with_wrong_data_types(base_url):
    invalid_booking = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": "two hundred",
        "depositpaid": "yes",
        "bookingdates": {"checkin": "2026-11-10", "checkout": "2026-11-15"},
        "additionalneeds": "Breakfast",
    }

    response = requests.post(f"{base_url}/booking", json=invalid_booking, timeout=10)

    assert response.status_code in [400, 422]
    assert response.elapsed.total_seconds() < 2
    assert response.text.strip() != ""
def test_get_nonexistent_booking(base_url):
    response = requests.get(
        f"{base_url}/booking/999999999",
        timeout=10
    )

    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 2

def test_update_booking_without_token(base_url, created_booking):
    booking_id = created_booking["booking_id"]

    updated_booking = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 400,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-20",
            "checkout": "2026-11-25"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(
        f"{base_url}/booking/{booking_id}",
        json=updated_booking,
        timeout=10
    )

    assert response.status_code == 403
    assert response.elapsed.total_seconds() < 2

def test_update_booking_with_wrong_token(base_url, created_booking):
    booking_id = created_booking["booking_id"]

    updated_booking = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 400,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-20",
            "checkout": "2026-11-25"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(
        f"{base_url}/booking/{booking_id}",
        json=updated_booking,
        headers={
            "Cookie": "token=wrongtoken123"
        },
        timeout=10
    )

    assert response.status_code == 403
    assert response.elapsed.total_seconds() < 2