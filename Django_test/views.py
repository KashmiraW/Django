from django.http import HttpResponse


def home(request):
    return HttpResponse("Hallo! Mijn eerste Django-pagina!")
    