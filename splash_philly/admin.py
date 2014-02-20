from __future__ import unicode_literals
from django.contrib import admin
from splash_philly.models import Pool
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields



class PoolAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }



admin.site.register(Pool, PoolAdmin)