from django.urls import path

from tickets.views import get_tickets

urlpatterns = [
    path("", get_tickets),
]
