from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.clsList)
class clsListsAdmin(admin.ModelAdmin):

    list_display = (
        "colName",
        "colUser",
        "def_Count_Rooms",
    )

    search_fields = ("^colName",)

    filter_horizontal = ("colRooms",)