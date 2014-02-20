
from django.core.exceptions import ValidationError
from django.http import request, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, View,ListView
from splash_philly.models import Pool
from splash_philly import settings
class HomeView(TemplateView):
    template_name = 'home.html'



class MapView(ListView):
    template_name = 'map.html'
    context = {'google_api_key' : settings.GOOGLE_API_KEY}
    def get_queryset(self):
        return Pool.objects.all()