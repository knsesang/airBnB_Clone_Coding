from django.contrib import admin
from . import models

#   썸네일 표시를 위해서 사용
#   보안을 위해서 태그 자동변환되는것 회피
from django.utils.html import mark_safe


# Register your models here.
#   어드민 패널에 + 가 생긴다
@admin.register(
    models.clsRoomType, models.clsAmenity, models.clsFacility, models.clsHouseRule
)
class clsItemAdmin(admin.ModelAdmin):

    list_display = (
        "colName",
        "def_Usedby",
    )

    def def_Usedby(self, obj):
        return obj.relRooms.count()

    def_Usedby.short_description = "Used By"


#   사진 선택하는것이 기본 3개까지 선택할수 있는 창으로 바뀜
#   inlines = (clsPhotoInline,) 도 같이 추가됨
#   TabularInline   : 캡션/파일선택/삭제버튼
#   StackedInline   : 삭제버튼<br/>캡션<br/>파일선택
class clsPhotoInline(admin.TabularInline):
    model = models.clsPhoto


@admin.register(models.clsRoom)
class clsRoomAdmin(admin.ModelAdmin):

    inlines = (clsPhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "colName",
                    "colDescription",
                    "colCountry",
                    "colCity",
                    "colAddress",
                    "colPrice",
                    "colRoom_type",
                ),
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "colCheck_in",
                    "colCheck_out",
                    "colInstant_book",
                ),
            },
        ),
        (
            "Space",
            {
                "fields": (
                    "colGuests",
                    "colBeds",
                    "colBedrooms",
                    "colBaths",
                ),
            },
        ),
        (
            "More Ablout the Space",
            {
                #   테이블 접음
                "classes": ("collapse",),
                "fields": (
                    "colAmenities",
                    "colFacilities",
                    "colHouse_rules",
                ),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("colHost",),
            },
        ),
    )

    #   목록 헤드 컬럼 선언
    list_display = (
        "colName",
        "colCountry",
        "colCity",
        "colPrice",
        "colAddress",
        "colGuests",
        "colBeds",
        "colBedrooms",
        "colBaths",
        "colCheck_in",
        "colCheck_out",
        "colInstant_book",
        "def_Count_Amenities",  #   Amenity 갯수
        "def_Count_Photos",  #   사진 갯수
        "def_Total_Rating",  #   방별 리뷰 점수
    )

    #   정렬
    """
    ordering = (
        "colName",
        "colPrice",
        "colBedrooms",
    )
    """

    # 필터, 빠른 선택
    list_filter = (
        "colInstant_book",
        "colHost__colSuperhost",
        "colHost__colGender",
        "colRoom_type",
        "colAmenities",
        "colFacilities",
        "colHouse_rules",
        "colCity",
        "colCountry",
    )

    #   목록에서 검색창 만들기
    #   search_fields=('city')
    #   ^ startwith
    #   = iexact
    #   @ search
    #   None icontains  대소문자 구분 안함

    #   추가전에는 host에 select 박스 형식이었지만
    #   이제는 검색해서 text 박스에 1개만 보여지는 형식으로 바뀜
    raw_id_fields = ("colHost",)

    search_fields = (
        "=colCity",
        "^colHost__username",  #   username 장고 기본 생성 컬럼
    )

    filter_horizontal = (
        "colAmenities",
        "colFacilities",
        "colHouse_rules",
    )

    #   Romm 별로 Amenity 갯수 구하는 함수
    #   obj : 현재 row
    def def_Count_Amenities(self, obj):

        #   print(obj)  #   방이름을 불러온다
        #   예쁜방

        #   print(obj.colAmenities.all())
        #   <QuerySet [<clsAmenity: wifi>, <clsAmenity: shower>]>

        return obj.colAmenities.count()

    #   short_description : 컬럼의 이름을 바꾼다
    def_Count_Amenities.short_description = "Amenity갯수"

    def def_Count_Photos(self, obj):
        return obj.relPhotos.count()

    #   short_description : 컬럼의 이름을 바꾼다
    def_Count_Photos.short_description = "Photo갯수"


@admin.register(models.clsPhoto)
class clsPhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "def_Get_Thumbnale",
    )

    def def_Get_Thumbnale(self, obj):
        #   print(dir(obj.colFile))

        #   print(obj.colFile.path)     #   /home/webRoot/django31_airBnB/uploads/room_photos/hotels.jpg
        #   print(obj.colFile.url)      #   /room_photos/hotels.jpg
        #   print(obj.colFile.width)    #   318
        #   print(obj.colFile.height)   #   159

        return mark_safe(f'<img width="50px" src="{obj.colFile.url}" />')

    def_Get_Thumbnale.short_description = "썸네일"