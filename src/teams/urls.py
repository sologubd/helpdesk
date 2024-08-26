from django.urls import path

from teams.views import Team, get_team_form

urlpatterns = [
    path("", Team.as_view()),
    path("<int:id>/", Team.as_view()),
    path("new/", get_team_form),
]
