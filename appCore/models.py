from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    varCreated = models.DateTimeField()
    varUpdated = models.DateTimeField()

    class Meta:
        #   데이타베이스에 나타나지 않는, 등록되지 모델 
        abstract = True         