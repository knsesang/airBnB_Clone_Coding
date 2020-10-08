from django.contrib import admin
from . import models


# Register your models here.


#   어드민 패널에 + 가 생긴다ㄴ
@admin.register(
    models.clsRoomType, models.clsAmenity, models.clsFacility, models.clsHouseRule
)
class clsItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.clsRoom)
class clsRoomAdmin(admin.ModelAdmin):

    #   목록 헤드 컬럼 선언
    list_display = (
        "varName",
        "varCountry",
        "varCity",
        "varPrice",
        "varAddress",
        "varGuests",
        "varBeds",
        "varBaths",
        "varCheck_in",
        "varCheck_out",
        "varInstant_book",
    )

    list_filter = (
        "varInstant_book",
        "varCountry",
        "varCity",
    )

    #   목록에서 검색창 만들기
    #   search_fields=('city')
    #   ^ startwith
    #   = iexact
    #   @ search
    #   None icontains  대소문자 구분 안함

    search_fields = (
        "=varCity",
        "^varHost__username",  #   username 기본 생성 컬럼
    )


@admin.register(models.clsPhoto)
class clsPhotoAdmin(admin.ModelAdmin):
    pass
