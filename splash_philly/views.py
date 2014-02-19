
from django.core.exceptions import ValidationError
from django.http import request, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, View,ListView
from splash_philly.models import Pool
class HomeView(TemplateView):
    template_name = 'home.html'
