from django.db import models
from appCore import models as core_models

# Create your models here.


class clsConversation(core_models.TimeStampedModel):

    #   Participants : 참가자
    varParticipants = models.ManyToManyField("appUsers.clsUser", blank=True)

    def __str__(self):
        return str(self.varCreated)


class clsMessage(core_models.TimeStampedModel):

    varMessage = models.TextField()
    varUser = models.ForeignKey("appUsers.clsUser", on_delete=models.CASCADE)
    varConversation = models.ForeignKey("clsConversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.varUser} says : {self.varMessage}"
