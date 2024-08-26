from django.http import HttpResponse
from django.template import loader


def get_messages(request):
    template = loader.get_template("message/list.jinja2")
    return HttpResponse(template.render())
