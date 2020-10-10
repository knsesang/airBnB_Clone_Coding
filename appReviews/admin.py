from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.clsReview)
class clsReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "def_Rating_Average",
    )
