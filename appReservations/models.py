from django.db import models

#   TimeStampedModel 불러오기용
from appCore import models as core_models

# 날짜 전후 비교용
from django.utils import timezone

from django.utils.dateparse import parse_date

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

    colStatus = models.CharField(
        choices=STATUS_CHOICES, default=STATUS_PENDING, max_length=12
    )
    colCheck_in = models.DateField(null=True)
    colCheck_out = models.DateField(null=True)

    colGuest = models.ForeignKey(
        "appUsers.clsUser", related_name="relReservations", on_delete=models.CASCADE
    )
    colRoom = models.ForeignKey(
        "appRooms.clsRoom", related_name="relReservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.colRoom}-{self.colCheck_in}"

    def def_In_Progress(self):
        #   now = timezone.now().date()     #   미국시간으로만 불러옴

        #   현재 한국시간 2020-10-11 02:04
        #   print(now)  #   2020-10-10
        #   print(timezone.datetime.now())  #   2020-10-10 17:03:49.322672
        #   print(timezone.datetime.today())  #   2020-10-10 17:03:49.322702ㅍ

        #   now = timezone.localtime()
        #   print(now)  #   2020-10-11 02:03:49.322733+09:00
        #   print(timezone.now())  #   2020-10-10 17:09:17.658301+00:00
        #   print(now.strftime("%Y-%m-%d"))  #   2020-10-11

        now = parse_date(timezone.localtime().strftime("%Y-%m-%d"))
        #   print(now)
        #   print(type(now))        #   <class 'datetime.date'>

        return now > self.colCheck_in and now < self.colCheck_out

    def def_Is_Finished(self):

        now = parse_date(timezone.localtime().strftime("%Y-%m-%d"))
        return now > self.colCheck_out

    #   True / False String 대신 O,X 로 나타나게 함
    def_In_Progress.boolean = True

    #   True / False String 대신 O,X 로 나타나게 함
    def_Is_Finished.boolean = True