from django.db import models
from appCore import models as core_models


# Create your models here.
class clsList(core_models.TimeStampedModel):

    colName = models.CharField(max_length=80, null=True)
    colUser = models.ForeignKey(
        "appUsers.clsUser", related_name="relLists", on_delete=models.CASCADE
    )
    colRooms = models.ManyToManyField(
        "appRooms.clsRoom", related_name="relLists", blank=True
    )

    def __str__(self):
        return self.colName

    def def_Count_Rooms(self):
        return self.colRooms.count()

    def_Count_Rooms.short_descriptions = "room갯수"