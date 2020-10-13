from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.

# admin.site.register(models.clsUser, clsCustomUserAdmin) = @admin.register(models.clsUser) 같은 표현 방식
#   어드민 패널에서 models.clsUser 를 보고싶다는 의미ㄴ
@admin.register(models.clsUser)
#   class clsCustomUserAdmin(admin.ModelAdmin):
class clsCustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "custom Profile",
            {
                "fields": (
                    "colAvatar",
                    "colGender",
                    "colBio",
                    "colBirthdate",
                    "colLanguage",
                    "colCurrency",
                    "colSuperhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("colSuperhost",)

    list_display = (
        "username",  #   장고 기본 모델에서 불러옴
        "first_name",  #   장고 기본 모델에서 불러옴
        "last_name",  #   장고 기본 모델에서 불러옴
        "email",  #   장고 기본 모델에서 불러옴
        "is_active",  #   장고 기본 모델에서 불러옴
        "colLanguage",
        "colCurrency",
        "colSuperhost",
        "is_staff",  #   장고 기본 모델에서 불러옴
        "is_superuser",  #   장고 기본 모델에서 불러옴
    )
