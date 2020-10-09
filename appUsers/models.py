from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class clsUser(AbstractUser):
    
    #   신규 추가하면 장고에 없으므로 오류날수 있다. 마이그레이션 필요
    
    #   다음은 기본값이 없다는 얘기이므로 default 값을 추가한다
    #   Please select a fix:
    #   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    #   2) Quit, and let me add a default in models.py

    varBio = models.TextField(default="")
