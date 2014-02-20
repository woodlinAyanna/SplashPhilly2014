
from django.core.exceptions import ValidationError
from django.http import request, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, View,ListView
from splash_philly.models import Pool
from splash_philly import settings
from googleplaces import GooglePlaces,types,lang


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'



class MapView(ListView):
    template_name = 'map.html'
    context = {'google_api_key' : settings.GOOGLE_API_KEY}
    def get_queryset(self):
        return Pool.objects.all()


class PlacesView(TemplateView):
    template_name = 'places.html'


    def get_context_data(self, **kwargs):
        context = super(PlacesView, self).get_context_data(**kwargs)
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)
        query_result = google_places.nearby_search(
        location='Philadelphia, PA', keyword='Pool',
        radius=20000)

        context['places'] = query_result
        return context
