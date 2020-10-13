from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.clsReservation)
class clsRevervationAdmin(admin.ModelAdmin):

    list_display = (
        "colRoom",
        "colStatus",
        "colCheck_in",
        "colCheck_out",
        "colGuest",
        "def_In_Progress",
        "def_Is_Finished",
    )

    list_filter = ("colStatus",)
