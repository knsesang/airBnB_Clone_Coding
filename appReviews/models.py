from django.db import models
from django.db.models.fields.related import ForeignKey
from appCore import models as core_models


# Create your models here.
class clsReview(core_models.TimeStampedModel):
    varReview = models.TextField()
    varCommunication = models.IntegerField()
    varCleanliness = models.IntegerField()
    varLocation = models.IntegerField()
    varCheck_in = models.IntegerField()
    varValue = models.IntegerField()

    #   리뷰를 쓰는 사람
    varUser = models.ForeignKey("appUsers.clsUser", on_delete=models.CASCADE)
    varRoom = models.ForeignKey("appRooms.clsRoom", on_delete=models.CASCADE)

    #   리뷰 제목이 clsReview object (1) 라고 나오는것을
    #   리뷰 제목이 나타날수 있도록 변경
    def __str__(self):

        return f"{self.varReview} - {self.varRoom}"
        #   리뷰 제목
        #   return self.varReview

        #   방이름
        #   return self.varRoom.varName

        #   방주인
        #   return self.varRoom.varHost

        #   방주인 이메일
        #   return self.varRoom.varHost.varEmail
        #   return self.varRoom.varHost.email
