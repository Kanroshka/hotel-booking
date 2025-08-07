from rest_framework import filters, mixins, viewsets

from booking.serializers import BookingCreateSerializers
from rooms.models import Room
from rooms.serializers import RoomCreateSerializer, RoomListSerializer


class RoomViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Room.objects.all()
    serializer_class = BookingCreateSerializers
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["cost", "created_at"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        return RoomListSerializer if self.action == "list" else RoomCreateSerializer
