from django.db import models

#   TimeStampedModel 불러오기용
from appCore import models as core_models


# Create your models here.
class clsReservation(core_models.TimeStampedModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    varStatus = models.CharField(
        choices=STATUS_CHOICES, default=STATUS_PENDING, max_length=12
    )
    varCheck_in = models.DateField(null=True)
    varCheck_out = models.DateField(null=True)

    varGuest = models.ForeignKey("appUsers.clsUser", on_delete=models.CASCADE)
    varRoom = models.ForeignKey("appRooms.clsRoom", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.varRoom}-{self.varCheck_in}"
