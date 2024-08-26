from django.http import HttpResponse
from django.template import loader


def get_tickets(request):
    template = loader.get_template("tickets/list.jinja2")
    return HttpResponse(template.render())
