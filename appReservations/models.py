from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import ModelChoiceField

#   TimeStampedModel 불러오기용
from appCore import models as core_models


# Create your models here.
class clsReservation(core_models.TimeStampedModel):

    STATUS_PENDINNG = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "cancled"

    STATUS_CHOICES = (
        (STATUS_PENDINNG, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCLED, "cancled"),
    )

    varStatus = models.CharField(
        choices=STATUS_CHOICES, default=STATUS_PENDINNG, max_length=50
    )
    varCheck_in = models.DateField(auto_now=False, auto_now_add=False)
    varCheck_out = models.DateField(auto_now=False, auto_now_add=False)

    varGuest = models.ForeignKey("appUsers.clsUser", on_delete=CASCADE)
    varRoom = models.ForeignKey("appRooms.clsRoom", on_delete=CASCADE)

    def __str__(self):
        return f"{self.varRoom}-{self.varCheck_in}"
