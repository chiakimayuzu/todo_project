from django.shortcuts import render
from django.views.generic import DetailView

class HomeView(DetailView):
    template_name = 'home.html'


class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

    