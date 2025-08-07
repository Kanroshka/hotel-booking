from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    description = models.TextField(blank=True, db_comment="Описание номера")
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
        null=False,
        blank=False,
        db_comment="Стоимоть номера",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_comment="Время открытия номера для бронирования"
    )

    class Meta:
        db_table = 'booking"."room'
        db_table_comment = "Номера в отелях"

    def __str__(self):
        return super().__str__()