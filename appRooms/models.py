from django.db import models
from django_countries.fields import CountryField
from appCore import models as core_models
from appUsers import models as user_models

from django.urls import reverse


class clsAbstractItem(core_models.TimeStampedModel):

    colName = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.colName


class clsRoomType(clsAbstractItem):
    class Meta:
        #   verbose_name_plural : 자동복수형 전환을 방지 ( clsRoomTypes X )
        verbose_name = "Room Type"

        #   생성된 날짜 순대로 정렬
        #   ordering = ["-colCreated"]

        #   ordering = ["-colName"]     역순

        ordering = ["colName"]


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
    colCaption = models.CharField(max_length=100)
    colFile = models.ImageField(upload_to="room_photos")

    #   파이썬은 위에서 아래로 실행한다.
    #   clsRoom 이 아래에 있으므로 실행 오류가 생길수 있다
    #   colRoom = models.ForeignKey(clsRoom, on_delete=models.CASCADE) 오류발생

    #   클래스 이름을 string 으로 지정하면 회피 가능ㄴ
    colRoom = models.ForeignKey(
        "clsRoom", related_name="relPhotos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.colCaption


# Create your models here.
class clsRoom(core_models.TimeStampedModel):
    colName = models.CharField(null=True, blank=True, max_length=140)
    colDescription = models.TextField(null=True, blank=True)
    colCountry = CountryField(null=True, blank=True)
    colCity = models.CharField(max_length=80, null=True, blank=True)
    colPrice = models.IntegerField(default=0)
    colAddress = models.CharField(max_length=140, null=True, blank=True)
    colGuests = models.IntegerField(default=0)
    colBeds = models.IntegerField(default=0)
    colBedrooms = models.IntegerField(default=0)
    colBaths = models.IntegerField(default=0)
    colCheck_in = models.TimeField(null=True)
    colCheck_out = models.TimeField(null=True)
    colInstant_book = models.BooleanField(default=False)
    colHost = models.ForeignKey(
        "appUsers.clsUser", related_name="relRooms", null=True, on_delete=models.CASCADE
    )

    colRoom_type = models.ForeignKey(
        "clsRoomType",
        related_name="relRooms",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    colAmenities = models.ManyToManyField(
        "clsAmenity", related_name="relRooms", blank=True
    )
    colFacilities = models.ManyToManyField(
        "clsFacility", related_name="relRooms", blank=True
    )
    colHouse_rules = models.ManyToManyField(
        "clsHouseRule", related_name="relRooms", blank=True
    )

    #   save 는 예약된 명령어를 호출하는것이므로 임의 변경이 불가능하다
    #   def_Save → def  로 변경
    def save(self, *args, **kwargs):

        #   사용자가 정의한 작업을 진행한다
        #   print(self.city)

        #   도시명의 첫 글자를 대문자로 바꾼다
        self.colCity = str.capitalize(self.colCity)

        #   원래 호출하려던 장고 내장함수를 호출해서 save 를 진행한다
        super().save(*args, **kwargs)  # call the real save() method

    """
    #   저장하려는 데이타 값들을 확인하고 저장할 수 있다
    def save_model(self, request, obj, form, change):
        print(obj, form, change)
       
        #   원래 호출하려던 장고 내장함수를 호출해서 save 를 진행한다
        super().save(*args, **kwargs)
    """

    #   어드민 수정 화면에 "view on site 버튼이 생김
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.colName

    #   방의 리뷰 평균
    def def_Total_Rating(self):
        all_reviews = self.relReviews.all()
        #   print(self.relReviews.all())

        #   all_ratings = []
        #   for review in all_reviews:
        #       print(review.def_Rating_Average())

        #   게시판 글 인용
        #   만약에 사용자가 방을 먼저 등록하고, 리뷰가 하나도 없다면 all_ratings=0가 됩니다.
        #   그러면 아래 코드에서 그러면 len(all_reviews)는 0임으로 ZeroDivisionError를 발생시킵니다.
        #   해결책은 예외처리 구문으로 해당 DivideByZero를 감싸면 됩니다.
        try:
            all_ratings = 0
            for review in all_reviews:
                all_ratings = all_ratings + review.def_Rating_Average()

            return all_ratings / len(all_reviews)

        except ZeroDivisionError:
            return 0
