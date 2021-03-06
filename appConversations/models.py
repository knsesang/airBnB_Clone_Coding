from django.db import models
from appCore import models as core_models

# Create your models here.


class clsConversation(core_models.TimeStampedModel):

    #   Participants : 참가자
    colParticipants = models.ManyToManyField(
        "appUsers.clsUser", related_name="clsConverstations", blank=True
    )

    def __str__(self):

        usernames = []

        for user in self.colParticipants.all():
            #   print(user.username)
            usernames.append(user.username)  #   username : clsUser 안의 장고 기본생성 컬럼

        return ", ".join(usernames)
        #   생성날짜
        #   return str(self.colCreated)

    def def_Count_Messages(self):
        return self.relMessages.count()

    def def_Count_Participants(self):
        return self.colParticipants.count()

    def_Count_Messages.short_description = "Message갯수"
    def_Count_Participants.short_description = "_Participants갯수ㄴ"


class clsMessage(core_models.TimeStampedModel):

    colMessage = models.TextField()
    colUser = models.ForeignKey(
        "appUsers.clsUser", related_name="relMessages", on_delete=models.CASCADE
    )
    colConversation = models.ForeignKey(
        "clsConversation", related_name="relMessages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.colUser} says : {self.colMessage}"
