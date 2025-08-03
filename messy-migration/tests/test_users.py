import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_get_all_users():
    response = app.test_client().get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_user_by_id():
    response = app.test_client().get("/user/1")  # assuming user with ID 1 exists
    assert response.status_code in [200, 404]  # depends if user exists or not

def test_login_route_exists():
    response = app.test_client().post("/login", json={"email": "test@example.com", "password": "test123"})
    # Even if login fails, the route should exist and return 200 or 401
    assert response.status_code in [200, 401]
