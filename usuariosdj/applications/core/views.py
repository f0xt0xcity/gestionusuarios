from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Hola</h1>')

class HomeView(TemplateView):

    template_name = 'home/index.html'