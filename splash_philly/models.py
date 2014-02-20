from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField
from django_google_maps import fields as map_fields






class Pool(models.Model):
    name = models.CharField(max_length=300)
    address = map_fields.AddressField(max_length=800)
    geolocation = map_fields.GeoLocationField(blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return "%s at %s" % (self.name,  self.address)


class Comment(models.Model):
    submitter = models.CharField(max_length=80)
    text =  models.CharField(max_length=400)
    posted = models.DateField()
    pool = models.ForeignKey(Pool,related_name='comments')
