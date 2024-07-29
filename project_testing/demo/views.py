from django.shortcuts import render
from demo.models import Message
from .serializers import MessageSerializer
from rest_framework.viewsets import ModelViewSet

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer