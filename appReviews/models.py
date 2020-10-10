from django.db import models
from appCore import models as core_models


# Create your models here.
class clsReview(core_models.TimeStampedModel):

    varReview = models.TextField(null=True)
    varAccuracy = models.IntegerField(default=0)
    varCommunication = models.IntegerField(default=0)
    varCleanliness = models.IntegerField(default=0)
    varLocation = models.IntegerField(default=0)
    varCheck_in = models.IntegerField(default=0)
    varValue = models.IntegerField(default=0)

    #   리뷰를 쓰는 사람
    varUser = models.ForeignKey("appUsers.clsUser", on_delete=models.CASCADE)
    varRoom = models.ForeignKey("appRooms.clsRoom", on_delete=models.CASCADE)

    def __str__(self):

        #   리뷰 제목이 clsReview object (1) 라고 나오는것을
        #   리뷰 제목이 나타날수 있도록 변경
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
