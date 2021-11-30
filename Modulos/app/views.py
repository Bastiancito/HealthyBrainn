from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'login.html'
#alalalaa
