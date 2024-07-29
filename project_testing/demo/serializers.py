from rest_framework import serializers
from demo.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user', 'text', 'created_at']