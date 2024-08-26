from django.http import HttpResponse
from django.template import loader
from django.views import View

from agents.models import Agent as AgentModel


def get_agent_form(request):
    template = loader.get_template("agents/new_agent.jinja2")
    return HttpResponse(template.render())


class Agents(View):
    def get(self, request):
        template = loader.get_template("agents/list.jinja2")
        return HttpResponse(template.render({"items": AgentModel.objects.all()}))

    def post(self, request):
        template = loader.get_template("agents/grid.jinja2")
        AgentModel.objects.create(
            first_name=request.POST.get("first-name"),
            last_name=request.POST.get("last-name"),
            email=request.POST.get("email"),
        )

        return HttpResponse(template.render({"items": AgentModel.objects.all()}))

    def delete(self, request, id):
        AgentModel.objects.filter(id=id).delete()
        return HttpResponse(b"")
