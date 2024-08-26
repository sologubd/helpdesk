from django.http import HttpResponse
from django.template import loader

from tickets.models import Status, Ticket


def dashboard(request):
    template = loader.get_template("helpdesk/dashboard.jinja2")

    return HttpResponse(
        template.render(
            {
                "in_progress": Ticket.objects.filter(status=Status.IN_PROGRESS).count(),
                "postponed": Ticket.objects.filter(status=Status.POSTPONED).count(),
                "resolved": Ticket.objects.filter(status=Status.RESOLVED).count(),
            }
        )
    )
