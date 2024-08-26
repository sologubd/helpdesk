from django.urls import path

from tickets.views import Tickets, get_ticket_form

urlpatterns = [
    path("", Tickets.as_view()),
    path("<int:id>", Tickets.as_view()),
    path("new/", get_ticket_form),
]
