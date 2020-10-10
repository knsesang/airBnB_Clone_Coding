from django.db import models
from appCore import models as core_models


# Create your models here.
class clsList(core_models.TimeStampedModel):

    varName = models.CharField(max_length=80, null=True)
    varUser = models.ForeignKey("appUsers.clsUser", on_delete=models.CASCADE)
    varRooms = models.ManyToManyField("appRooms.clsRoom", blank=True)

    def __str__(self):
        return self.varName
