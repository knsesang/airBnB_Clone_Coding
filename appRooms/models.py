from django.db import models
from django_countries.fields import CountryField
from appCore import models as core_models
from appUsers import models as user_models


class clsAbstractItem(core_models.TimeStampedModel):

    varName = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.varName


class clsRoomType(clsAbstractItem):
    class Meta:
        #   verbose_name_plural : 자동복수형 전환을 방지 ( clsRoomTypes X )
        verbose_name = "Room Type"

        #   생성된 날짜 순대로 정렬
        #   ordering = ["-varCreated"]

        #   ordering = ["-varName"]     역순

        ordering = ["varName"]


class clsAmenity(clsAbstractItem):
    class Meta:
        #   verbose_name_plural : 자동복수형 전환을 방지 ( clsAmenitys X )
        verbose_name_plural = "Amenities"


class clsFacility(clsAbstractItem):
    class Meta:
        #   verbose_name_plural : 자동복수형 전환을 방지 ( clsFacilitys X )
        verbose_name_plural = "Facilities"


class clsHouseRule(clsAbstractItem):
    class Meta:
        #   verbose_name : 자동 소문자 전환을 방지 ( House rule X )
        verbose_name = "House Rule"


class clsPhoto(core_models.TimeStampedModel):
    varCaption = models.CharField(max_length=100)
    varFile = models.ImageField()

    #   파이썬은 위에서 아래로 실행한다.
    #   clsRoom 이 아래에 있으므로 실행 오류가 생길수 있다
    #   varRoom = models.ForeignKey(clsRoom, on_delete=models.CASCADE) 오류발생

    #   클래스 이름을 string 으로 지정하면 회피 가능ㄴ
    varRoom = models.ForeignKey(
        "clsRoom", related_name="relPhotos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.varCaption


# Create your models here.
class clsRoom(core_models.TimeStampedModel):
    varName = models.CharField(null=True, blank=True, max_length=140)
    varDescription = models.TextField(null=True, blank=True)
    varCountry = CountryField(null=True, blank=True)
    varCity = models.CharField(max_length=80, null=True, blank=True)
    varPrice = models.IntegerField(default=0)
    varAddress = models.CharField(max_length=140, null=True, blank=True)
    varGuests = models.IntegerField(default=0)
    varBeds = models.IntegerField(default=0)
    varBedrooms = models.IntegerField(default=0)
    varBaths = models.IntegerField(default=0)
    varCheck_in = models.TimeField(null=True)
    varCheck_out = models.TimeField(null=True)
    varInstant_book = models.BooleanField(default=False)
    varHost = models.ForeignKey(
        "appUsers.clsUser", related_name="relRooms", null=True, on_delete=models.CASCADE
    )

    varRoom_type = models.ForeignKey(
        "clsRoomType",
        related_name="relRooms",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    varAmenities = models.ManyToManyField(
        "clsAmenity", related_name="relRooms", blank=True
    )
    varFacilities = models.ManyToManyField(
        "clsFacility", related_name="relRooms", blank=True
    )
    varHouse_rules = models.ManyToManyField(
        "clsHouseRule", related_name="relRooms", blank=True
    )

    def __str__(self):
        return self.varName

    #   방의 리뷰 평균
    def def_Total_Rating(self):
        all_reviews = self.relReviews.all()
        #   print(self.relReviews.all())

        all_ratings = []
        for review in all_reviews:
            print(review.def_Rating_Average())
            all_ratings.append(review.def_Rating_Average())

        return 0
