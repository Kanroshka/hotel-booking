from rest_framework import serializers

from rooms.models import Room


class RoomCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Room
        fields=("room_id", "description", "cost")
        read_only_fields=("room_id",)
        extra_kwargs = {
            "description": {"write_only": True},
            "cost": {"write_only": True},
        }



class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=("room_id", "description", "cost")
