import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def auth_token(base_url):
    response = requests.post(
        f"{base_url}/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        timeout=10
    )

    assert response.status_code == 200

    token = response.json()["token"]

    return token

@pytest.fixture
def booking_data():
    return {
        "firstname": "Queen",
        "lastname": "Uwase",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-10",
            "checkout": "2026-11-15"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture
def created_booking(base_url, booking_data):
    response = requests.post(
        f"{base_url}/booking",
        json=booking_data,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    return {
        "booking_id": data["bookingid"],
        "booking": data["booking"]
    }