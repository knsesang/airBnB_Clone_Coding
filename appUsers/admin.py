from django.contrib import admin
from . import models


# Register your models here.

# admin.site.register(models.clsUser, clsCustomUserAdmin) = @admin.register(models.clsUser) 같은 표현 방식
#   어드민 패널에서 models.clsUser 를 보고싶다는 의미ㄴ
@admin.register(models.clsUser)
class clsCustomUserAdmin(admin.ModelAdmin):

    #   email 이메일은 장고 기본 모델에서 불러옴
    list_display = (
        "username",
        "email",
        "varGender",
        "varLanguage",
        "varCurrency",
        "varSuperhost",
    )

    list_filter = (
        "varLanguage",
        "varCurrency",
        "varSuperhost",
    )
