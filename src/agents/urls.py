from django.urls import path
from agents.views import get_agents

urlpatterns = [
    path("", get_agents),
]
