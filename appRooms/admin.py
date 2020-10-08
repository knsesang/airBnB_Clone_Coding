from django.contrib import admin
from django.contrib.admin.options import HORIZONTAL
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

    fieldsets = (
        (
            "basic Info",
            {
                "fields": (
                    "varName",
                    "varDescription",
                    "varCountry",
                    "varAddress",
                    "varPrice",
                ),
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "varCheck_in",
                    "varCheck_out",
                    "varInstant_book",
                ),
            },
        ),
        (
            "More Ablout the Space",
            {
                #   테이블 접음
                "classes": ("collapse",),
                "fields": (
                    "varAmenities",
                    "varFacilities",
                    "varHouse_rules",
                ),
            },
        ),
        (
            "Space",
            {
                "fields": (
                    "varGuests",
                    "varBedrooms",
                    "varBaths",
                ),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("varHost",),
            },
        ),
    )

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
        "def_CountAmenities",
    )

    #   정렬
    ordering = (
        "varName",
        "varPrice",
        "varBedrooms",
    )

    # 필터 빠른 선택
    list_filter = (
        "varInstant_book",
        "varHost__varSuperhost",
        "varHost__varGender",
        "varRoom_type",
        "varAmenities",
        "varFacilities",
        "varHouse_rules",
        "varCity",
        "varCountry",
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

    filter_horizontal = (
        "varAmenities",
        "varFacilities",
        "varHouse_rules",
    )

    #   Room 별로 Amenity 갯수 구하는 함수
    #   obj : 현재 row
    def def_CountAmenities(self, obj):

        print(obj)  #   방이름을 불러온다
        #   예쁜방

        print(obj.varAmenities.all())
        #   <QuerySet [<clsAmenity: wifi>, <clsAmenity: shower>]>

        #   amenity 갯수 반환
        return obj.varAmenities.count()
        #   <QuerySet [<clsAmenity: wifi>, <clsAmenity: shower>]>

    #   short_description : 컬럼의 이름을 바꾼다
    def_CountAmenities.short_description = "Amenity Count"


@admin.register(models.clsPhoto)
class clsPhotoAdmin(admin.ModelAdmin):
    pass
