from django.http import HttpResponse
from django.template import loader


def dashboard(request):
    template = loader.get_template("helpdesk/dashboard.jinja2")
    return HttpResponse(template.render())
