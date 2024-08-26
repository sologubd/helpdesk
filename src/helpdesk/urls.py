from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from helpdesk.views import dashboard

urlpatterns = [
    path("", dashboard),
    path("admin/", admin.site.urls),
    # internal apps
    path("addresses/", include("addresses.urls")),
    path("agents/", include("agents.urls")),
    # path("message/", include("message.urls")),
    path("teams/", include("teams.urls")),
    path("tickets/", include("tickets.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
