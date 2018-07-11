from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Header, Service_Section
# Create your views here.
def index(request):
	header = Header.objects.all()
	service_section = Service_Section.objects.all()
	context = {
        'header': header,
        'service_section':service_section
    }
	return render_to_response('index.html',context,context_instance=RequestContext(request))
