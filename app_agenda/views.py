from django.shortcuts import render
from django.views.generic import ListView


from .models import AgendaPublica

class HomePageView(ListView):
    model = AgendaPublica
    template_name = 'app_agenda/home.html'

