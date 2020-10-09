from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.clsUser)
class clsCustomUserAdmin(admin.ModelAdmin):
    
    pass
