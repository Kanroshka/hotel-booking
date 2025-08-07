import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_booking_creation_and_overlap(room_factory, api_client):
    room = room_factory()

    resp1 = api_client.post(
        "/bookings/create",
        {
            "room_id": room.room_id,
            "date_start": "2025-09-10",
            "date_end": "2025-09-12",
        },
    )
    assert resp1.status_code == status.HTTP_201_CREATED

    resp2 = api_client.post(
        "/bookings/create",
        {
            "room_id": room.room_id,
            "date_start": "2025-09-11",
            "date_end": "2025-09-13",
        },
    )
    assert resp2.status_code == status.HTTP_400_BAD_REQUEST


def test_booking_list_sorted(booking_factory, api_client):
    b3 = booking_factory(date_start="2025-12-10", date_end="2025-12-12")
    need_room = b3.room_id
    b1 = booking_factory(
        date_start="2025-08-05", date_end="2025-08-08", room_id=need_room
    )
    b2 = booking_factory(
        date_start="2025-09-01", date_end="2025-09-03", room_id=need_room
    )

    resp = api_client.get(f"/bookings/list?room_id={need_room.room_id}")
    print(resp.data)
    ids = [b["booking_id"] for b in resp.data]
    assert ids == [b1.booking_id, b2.booking_id, b3.booking_id]
