from django.shortcuts import render, redirect

from core.models import *
from core.forms import ContactForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()


    context = {
        'services' : Service.objects.all(),
        'projects' : Project.objects.all(),
        'team' : Team.objects.all(),
        'gallery' : Gallery.objects.all(),
        'forms' : form,
        'testimonials' : Testimonials.objects.all(),


    }

    return render(request, 'index.html', context)


def services(request, slug):
    context = {
        'services' : Service.objects.get(slug = slug),

    }

    return render(request, 'services.html', context)