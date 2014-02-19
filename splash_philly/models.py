from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField






class Pool(models.Model):
    name = models.CharField(max_length=300)
    street_address =models.CharField(max_length=400)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state =  USStateField(choices = STATE_CHOICES)

