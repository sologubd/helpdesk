from django.http import HttpResponse
from django.template import loader
from django.views import View

from addresses.models import Address as AddressModel


class Address(View):
    def get(self, request):
        template = loader.get_template("addresses/list.jinja2")
        return HttpResponse(template.render({"items": AddressModel.objects.all()}))

    def post(self, request):
        template = loader.get_template("addresses/grid.jinja2")
        AddressModel.objects.create(
            email=request.POST.get("email"),
            description=request.POST.get("description"),
        )
        return HttpResponse(
            template.render({"items": AddressModel.objects.all()}),
        )

    def delete(self, request, id):
        AddressModel.objects.filter(id=id).delete()

        return HttpResponse(b"")


def get_address_form(request):
    template = loader.get_template("addresses/new_address.jinja2")
    return HttpResponse(template.render())
