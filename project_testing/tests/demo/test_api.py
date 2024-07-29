import pytest
from rest_framework.test import APIClient
from demo.models import Message
from django.contrib.auth.models import User
import json

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_get_messages(client):
    # Arrange - подготовка данных
    User.objects.create_user('admin')
    Message.objects.create(user_id=1, text='test_2')
    # Act - тестируемый функционал
    responce = client.get('/messages/')
    # Assert - сам тест
    assert responce.status_code == 200
    data = responce.json()
    assert len(data) == 1
    assert data[0]['text'] == 'test_2'
    

@pytest.mark.django_db
def test_create_messages(client):
    User.objects.create_user('admin')
    response = client.post('/messages/', data={'user': 1, 'text': 'test_1'}, format='json')
    
    assert response.status_code == 201