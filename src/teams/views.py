from django.http import HttpResponse
from django.template import loader
from django.views import View

from addresses.models import Address as AddressModel
from teams.models import Team as TeamModel


class Team(View):
    def get(self, request):
        template = loader.get_template("teams/list.jinja2")
        teams = TeamModel.objects.all()
        return HttpResponse(template.render({"items": teams}))

    def post(self, request):
        template = loader.get_template("teams/grid.jinja2")
        TeamModel.objects.create(
            name=request.POST.get("name"),
            email_id=request.POST.get("email"),
        )

        return HttpResponse(template.render({"items": TeamModel.objects.all()}))

    def delete(self, request, id):
        TeamModel.objects.filter(id=id).delete()
        return HttpResponse(b"")


def get_team_form(request):
    template = loader.get_template("teams/new_team.jinja2")
    address_list = [{"id": None, "email": "Choose Email"}]
    address_list.extend([{"id": address.id, "email": address.email} for address in AddressModel.objects.all()])
    return HttpResponse(template.render({"addresses": address_list}))
