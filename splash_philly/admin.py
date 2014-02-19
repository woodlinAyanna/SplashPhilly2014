__author__ = 'matt'
from django.contrib import admin
from splash_philly.models import Pool


class PoolAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pool, PoolAdmin)