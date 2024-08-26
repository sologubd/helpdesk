from django.urls import path
from addresses.views import Address
from addresses.views import get_address_form


urlpatterns = [
    path("", Address.as_view()),
    path("<int:id>/", Address.as_view()),
    path("new-address/", get_address_form),
]
