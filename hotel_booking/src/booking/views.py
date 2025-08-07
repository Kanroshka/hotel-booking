from datetime import date

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from booking.models import Booking
from booking.serializers import BookingCreateSerializers, BookingListSerializer


class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

    def get_queryset(self):
        room_id = self.request.query_params.get("room_id")
        if not room_id:
            raise ValidationError({"room_id": "Обязательный параметр."})
        return self.queryset.filter(room_id=room_id).order_by("date_start")


class BookingDeleteAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "booking_id"

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)

        return Response(
            {"booking_id": kwargs.get(self.lookup_field)}, status=status.HTTP_200_OK
        )

    def perform_destroy(self, instance):
        if instance.date_end < date.today():
            raise ValidationError({"date_start": "Уже слишком поздно отменять бронь."})

        instance.delete()


class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializers

    def perform_create(self, serializer):
        booking = serializer.validated_data

        is_conflict = Booking.objects.filter(
            room_id=booking.get("room_id"),
            date_start__lt=booking.get("date_end"),
            date_end__gt=booking.get("date_start"),
        ).exists()
        if is_conflict:
            raise ValidationError({"Error": "Имеются пересечения в бронировании"})

        serializer.save()
