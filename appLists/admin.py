from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.clsList)
class clsListsAdmin(admin.ModelAdmin):
    pass
