from django.http import HttpResponse
from django.template import loader


def get_agents(request):
    template = loader.get_template("agents/list.jinja2")
    return HttpResponse(template.render())
