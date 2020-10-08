from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.clsReservation)
class clsRevervationAdmin(admin.ModelAdmin):
    pass
