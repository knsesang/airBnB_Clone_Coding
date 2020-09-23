from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.clsRoom)
class clsRoomAdmin(admin.ModelAdmin):
    pass

