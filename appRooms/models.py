from django.db import models
from django_countries.fields import CountryField
from appCore import models as core_models

from appUsers import models as user_models

# Create your models here.
class clsRoom(core_models.TimeStampedModel):
    varName = models.CharField(max_length=140)
    varDescription = models.TextField(null=True, blank=True)
    varCountry = CountryField()
    varCity = models.CharField(max_length=80)
    varPrice = models.IntegerField(default=0)
    varAddress = models.CharField(max_length=140,null=True, blank=True )
    varGuests = models.IntegerField(default=0)
    varBeds = models.IntegerField(default=0)
    varBaths = models.IntegerField(default=0)
    varCheck_in = models.TimeField()
    varCheck_out = models.TimeField()
    varInstant_book = models.BooleanField(default=False)
    varHost = models.ForeignKey(user_models.clsUser, on_delete=models.CASCADE)

