from django.urls import path

from addresses.views import Address, get_address_form

urlpatterns = [
    path("", Address.as_view()),
    path("<int:id>/", Address.as_view()),
    path("new/", get_address_form),
]
