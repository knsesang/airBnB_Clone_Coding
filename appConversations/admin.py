from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.clsMessage)
class clsMessageAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "colCreated",
    )


@admin.register(models.clsConversation)
class clsConversationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "def_Count_Messages",
        "def_Count_Participants",
    )
