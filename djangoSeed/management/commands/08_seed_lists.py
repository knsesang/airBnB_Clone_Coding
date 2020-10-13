from django.core.management.base import BaseCommand
from django_seed import Seed
from appLists import models as list_models
from appUsers import models as user_models
from appRooms import models as room_models
from django.contrib.admin.utils import flatten

import random

NAME = "lists"


class Command(BaseCommand):
    help = "this command creates lists"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        users = user_models.clsUser.objects.all()
        rooms = room_models.clsRoom.objects.all()

        seeder.add_entity(
            list_models.clsList,
            numbers,
            {
                "colUser": lambda x: random.choice(users),
            },
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = list_models.clsList.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]

            #   list_model.clsRooms.add(to_add) 가 아닌 이유
            #   to_add 가 array 이기때문에
            list_model.colRooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} lists ccreated"))