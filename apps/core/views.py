from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

    
def home(request):
    return render_to_response("core/home.html", {'user': 'Martin'}, RequestContext(request))

def example_00(request):
    return HttpResponse("<html><b>Esto es HTML crudo!!</b></html>", RequestContext(request))

def example_01(request):
    return render_to_response("core/home.html", {}, RequestContext(request))

def example_02(request):
    return render_to_response("core/home.html", {'user': 'Martin'}, RequestContext(request))