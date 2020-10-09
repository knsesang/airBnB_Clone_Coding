from django.db import models
from django_countries.fields import CountryField
from appCore import models as core_models
from appUsers import models as user_models


class clsAbstractItem(core_models.TimeStampedModel):

    varName = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.varName


class clsRoomType(clsAbstractItem):
    pass


class clsAmenity(clsAbstractItem):
    pass


class clsFacility(clsAbstractItem):
    pass


class clsHouseRule(clsAbstractItem):
    pass


# Create your models here.
class clsRoom(core_models.TimeStampedModel):
    varName = models.CharField(null=True, blank=True, max_length=140)
    varDescription = models.TextField(null=True, blank=True)
    varCountry = CountryField(null=True, blank=True)
    varCity = models.CharField(max_length=80, null=True, blank=True)
    varPrice = models.IntegerField(default=0)
    varAddress = models.CharField(max_length=140, null=True, blank=True)
    varGuests = models.IntegerField(default=0)
    varBeds = models.IntegerField(default=0)
    varBedrooms = models.IntegerField(default=0)
    varBaths = models.IntegerField(default=0)
    varCheck_in = models.TimeField(null=True)
    varCheck_out = models.TimeField(null=True)
    varInstant_book = models.BooleanField(default=False)
    varHost = models.ForeignKey(
        user_models.clsUser, null=True, on_delete=models.CASCADE
    )

    varRoom_type = models.ForeignKey(
        clsRoomType, on_delete=models.SET_NULL, null=True, blank=True
    )
    varAmenities = models.ManyToManyField(clsAmenity, blank=True)
    varFacilities = models.ManyToManyField(clsFacility, blank=True)
    varHouse_rules = models.ManyToManyField(clsHouseRule, blank=True)

    def __str__(self):
        return self.varName
