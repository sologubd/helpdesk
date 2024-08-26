from django.urls import path

from agents.views import Agents, get_agent_form

urlpatterns = [
    path("", Agents.as_view()),
    path("<int:id>/", Agents.as_view()),
    path("new/", get_agent_form),
]
