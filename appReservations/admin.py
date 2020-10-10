from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.clsReservation)
class clsRevervationAdmin(admin.ModelAdmin):

    list_display = (
        "varRoom",
        "varStatus",
        "varCheck_in",
        "varCheck_out",
        "varGuest",
        "def_In_Progress",
        "def_Is_Finished",
    )

    list_filter = ("varStatus",)
