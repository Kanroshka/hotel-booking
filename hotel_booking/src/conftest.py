import factory
import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from booking.models import Booking
from rooms.models import Room


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    room_id = factory.SubFactory(RoomFactory)


@pytest.fixture
def api_client():
    return APIClient()


register(RoomFactory)
register(BookingFactory)
