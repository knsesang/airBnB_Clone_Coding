from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.clsMessage)
class clsMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.clsConversation)
class clsConversationAdmin(admin.ModelAdmin):
    pass