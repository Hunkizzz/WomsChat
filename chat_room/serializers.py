from rest_framework import serializers
from django.contrib.auth.models import User
from chat_room.models import Room, Chat

class UserSerializer(serializers.ModelSerializer):
    # Сериалиация пользователя
        # Сериализация комнат чата
    class Meta:
        model = User
        fields = ("id","username")

class RoomSerializers(serializers.ModelSerializer):
    # Сериализация комнат чата
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ("creater","invited","date")

class ChatSerializers(serializers.ModelSerializer):
    # Сериализация чата
    user = UserSerializer()
    class Meta:
        model = Chat
        fields = ("user", "text", "date")

class ChatPostSerializers(serializers.ModelSerializer):
        class Meta:
            model = Chat
            fields = ("room","text")
