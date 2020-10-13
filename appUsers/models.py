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

    #   choice : 앞은 DB에, 뒤는 호면 노출용 값

    # 파이썬 list, tuple 차이 : https://itholic.github.io/python-list-tuple/
    # () [] {}의 차이와 사용해야 할 곳 : https://hashcode.co.kr/questions/4118/%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%99%80-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC-%ED%95%A0-%EA%B3%B3

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_KOREAN = "kor"
    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_OTHER = "other"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "korean"),
        (LANGUAGE_ENGLISH, "english"),
        (LANGUAGE_OTHER, "other"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_OTHER = "other"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "dollar"),
        (CURRENCY_KRW, "won"),
        (CURRENCY_OTHER, "other"),
    )

    colGender = models.CharField(
        choices=GENDER_CHOICES,
        default=GENDER_MALE,
        max_length=10,
        null=True,
        blank=True,
    )

    colLanguage = models.CharField(
        choices=LANGUAGE_CHOICES,
        default=LANGUAGE_KOREAN,
        max_length=10,
        null=True,
        blank=True,
    )

    colCurrency = models.CharField(
        choices=CURRENCY_CHOICES,
        default=CURRENCY_KRW,
        max_length=10,
        null=True,
        blank=True,
    )

    colAvatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    colBio = models.TextField(default="", blank=True)
    colBirthdate = models.DateTimeField(null=True, blank=True)
    colSuperhost = models.BooleanField(default=False)
