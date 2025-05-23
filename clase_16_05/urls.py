from django.contrib import admin
from django.urls import path
from clase_16_05.views import ChatBotViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('chatear', ChatBotViewSet, basename='chatbot')

urlpatterns = [
]

urlpatterns += router.urls