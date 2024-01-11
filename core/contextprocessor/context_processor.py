from core.models import About

def footer_about(request):
    context = {
        'about' : About.objects.first()
    }

    return context