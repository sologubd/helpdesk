from django.http import HttpResponse
from django.template import loader
from django.views import View

from teams.models import Team as TeamModel
from tickets.models import Status
from tickets.models import Ticket as TicketModel


def get_ticket_form(request):
    template = loader.get_template("tickets/new_ticket.jinja2")
    status_choices = Status.choices
    return HttpResponse(
        template.render(
            {
                "statuses": status_choices,
                "teams": TeamModel.objects.all(),
            }
        )
    )


class Tickets(View):
    def get(self, request):
        template = loader.get_template("tickets/list.jinja2")
        return HttpResponse(template.render({"items": TicketModel.objects.all()}))

    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        assigned_to_id = request.POST.get("assigned-to")

        TicketModel.objects.create(
            title=title,
            description=description,
            assigned_to_id=assigned_to_id,
        )

        template = loader.get_template("tickets/grid.jinja2")
        return HttpResponse(template.render({"items": TicketModel.objects.all()}))
