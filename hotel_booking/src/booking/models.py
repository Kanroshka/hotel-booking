from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q

from rooms.models import Room


def validate_date_start(value):
    if value <= date.today():
        raise ValidationError("Дата брони уже прошла(")


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    date_start = models.DateField(
        null=False, validators=[validate_date_start], db_comment="Дата заезда"
    )
    date_end = models.DateField(null=False, db_comment="Дата выезда")
    room_id = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_column="room_id",
        db_comment="Ссылка на забронированный номер",
    )

    class Meta:
        db_table = 'booking"."booking'
        db_table_comment = "Бронирования номеров отеля"
        constraints = [
            models.CheckConstraint(
                check=Q(date_end__gt=F("date_start")), name="booking_end_after_start"
            ),
        ]

    def __str__(self):
        return ""
