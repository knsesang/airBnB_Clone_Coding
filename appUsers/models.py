from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class clsUser(AbstractUser):
    
    #   신규 추가하면 장고에 없으므로 오류날수 있다. 마이그레이션 필요
    
    #   다음은 기본값이 없다는 얘기이므로 default 값을 추가한다
    #   Please select a fix:
    #   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    #   2) Quit, and let me add a default in models.py


    #   null=True 는 DB 용, 
    #   blank=True 는  form용. 누락시 필수값이라고 나타남
    varAvartar = models.ImageField(null=True, blank=True)
    varBio = models.TextField(default="", blank=True)

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = [
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    ]

    varGender = models.CharField(
        choices=GENDER_CHOICES, 
        default=GENDER_MALE, 
        max_length = 10, 
        null=True, 
        blank=True)

    varBirthDate = models.DateTimeField(null=True,  blank=True)

    LANGUAGE_KOREAN = "korean"
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_OTHER = "other"

    LANGUAGE_CHOICES = [
        (LANGUAGE_KOREAN, "korean"),
        (LANGUAGE_ENGLISH, "english"),
        (LANGUAGE_OTHER, "other"),
    ]

    varLanguage = models.CharField(
        choices=LANGUAGE_CHOICES, 
        default=LANGUAGE_KOREAN, 
        max_length = 10, 
        null=True, 
        blank=True)


    CURRENCY_USD = "usd"
    CURRENCY_WON = "krw"
    CURRENCY_OTHER = "other"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "usd"),
        (CURRENCY_WON, "krw"),
        (CURRENCY_OTHER, "other"),
    ]

    varCurrency = models.CharField(
        choices=CURRENCY_CHOICES, 
        default=CURRENCY_WON, 
        max_length = 10, 
        null=True, 
        blank=True)

    varSuperhost = models.BooleanField(default=False)
    