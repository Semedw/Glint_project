from django.shortcuts import render

from core.models import *

# Create your views here.


def home(request):
    context = {
        'about' : About.objects.first().content,
        'services' : Service.objects.all(),
        'projects' : Project.objects.all(),
        'team' : Team.objects.all(),

    }

    return render(request, 'index.html', context)


def services(request, slug):
    context = {
        'services' : Service.objects.get(slug = slug),

    }

    return render(request, 'services.html', context)