import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_create_room(api_client):
    resp = api_client.post("/rooms", {"description": "Deluxe", "cost": 450000})
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data.get("room_id") is not None


def test_list_room_ordering(room_factory, api_client):
    room_factory(cost=13.12)
    room_factory(cost=10000)

    resp = api_client.get("/rooms?ordering=cost")
    costs = [room["cost"] for room in resp.data]
    assert costs == sorted(costs, reverse=True)
