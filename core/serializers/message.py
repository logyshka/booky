from rest_framework import serializers

from .user import UserSerializer
from ..models import Message


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'user', 'book', 'text', 'updated_at', 'created_at']
        read_only_fields = ['user']
