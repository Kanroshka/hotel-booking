from datetime import date

from django.core.exceptions import ValidationError
from rest_framework import serializers

from booking.models import Booking
from rooms.models import Room


class BookingCreateSerializers(serializers.ModelSerializer):
    booking_id = serializers.IntegerField(read_only=True)
    date_start = serializers.DateField(write_only=True)
    date_end = serializers.DateField(write_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), write_only=True
    )

    def validate_date_start(self, val):
        if val <= date.today():
            raise ValidationError("Дата брони уже прошла(")
        return val

    def validate(self, data):
        if data["date_start"] > data["date_end"]:
            raise ValidationError("Ошибка в датах: date_start > date_end")
        return data

    class Meta:
        model = Booking
        fields = ("booking_id", "date_start", "date_end", "room_id")


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("booking_id", "date_start", "date_end")
