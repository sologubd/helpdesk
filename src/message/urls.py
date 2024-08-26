from django.urls import path

from message.views import get_messages

urlpatterns = [
    path("", get_messages),
]
