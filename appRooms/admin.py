from django.contrib import admin
from . import models


# Register your models here.


#   어드민 패널에 + 가 생긴다ㄴ
@admin.register(models.clsRoomType)
class clsItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.clsRoom)
class clsRoomAdmin(admin.ModelAdmin):
    pass
