from django.db import models
from appCore import models as core_models


# Create your models here.
class clsReview(core_models.TimeStampedModel):

    colReview = models.TextField(null=True)
    colAccuracy = models.IntegerField(default=0)
    colCommunication = models.IntegerField(default=0)
    colCleanliness = models.IntegerField(default=0)
    colLocation = models.IntegerField(default=0)
    colCheck_in = models.IntegerField(default=0)
    colValue = models.IntegerField(default=0)

    #   리뷰를 쓰는 사람
    colUser = models.ForeignKey(
        "appUsers.clsUser", related_name="relReviews", on_delete=models.CASCADE
    )
    colRoom = models.ForeignKey(
        "appRooms.clsRoom", related_name="relReviews", on_delete=models.CASCADE
    )

    def __str__(self):

        #   리뷰 제목이 clsReview object (1) 라고 나오는것을
        #   리뷰 제목이 나타날수 있도록 변경
        return f"{self.colReview} - {self.colRoom}"

        #   리뷰 제목
        #   return self.colReview

        #   방이름
        #   return self.colRoom.colName

        #   방주인
        #   return self.colRoom.colHost

        #   방주인 이메일
        #   return self.colRoom.colHost.colEmail
        #   return self.colRoom.colHost.email

    #   방의 평점은 어드민에서만 보여지지 않으므로
    #   model 에 함수를 추가한다
    def def_Rating_Average(self):
        avg = (
            self.colAccuracy
            + self.colCommunication
            + self.colCleanliness
            + self.colLocation
            + self.colCheck_in
            + self.colValue
        ) / 6

        #   1.6666666666666667
        #   소숫점 2자리 올림
        return round(avg, 2)

    def_Rating_Average.short_description = "리뷰평균"