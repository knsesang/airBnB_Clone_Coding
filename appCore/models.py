from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):

    #   auto_now = True : 필드가 모델을 save  할때마다 date, time   기록
    #   auto_now_add = True : 모델을 생성할때마다 date, time   기록

    varCreated = models.DateTimeField(auto_now_add=True)
    varUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        #   데이타베이스에 나타나지 않는, 등록되지 모델
        abstract = True
