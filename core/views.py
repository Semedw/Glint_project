from django.shortcuts import render

from core.models import *

# Create your views here.


def home(request):
    context = {
        'about' : About.objects.first().content,
        'services' : Service.objects.all(),
        'projects' : Project.objects.all()
    }

    return render(request, 'index.html', context)