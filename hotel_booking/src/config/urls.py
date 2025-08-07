from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from booking.views import BookingCreateAPIView, BookingDeleteAPIView, BookingListAPIView
from rooms.views import RoomViewSet

router = SimpleRouter(trailing_slash="")
router.register(r"rooms", RoomViewSet, basename="room")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bookings/list", BookingListAPIView.as_view()),
    path("booking/<int:booking_id>", BookingDeleteAPIView.as_view()),
    path("bookings/create", BookingCreateAPIView.as_view()),
    path("", include(router.urls)),
]
