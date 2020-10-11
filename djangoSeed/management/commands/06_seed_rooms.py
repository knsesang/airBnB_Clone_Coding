from django.core.management.base import BaseCommand
from django_seed import Seed

from appRooms import models as room_models
from appUsers import models as user_models

import random


class Command(BaseCommand):
    help = "this command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=2, type=int, help="how many?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")

        all_users = user_models.clsUser.objects.all()
        room_types = room_models.clsRoomType.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(
            room_models.clsRoom,
            numbers,
            {
                "varName": lambda x: seeder.faker.address(),
                "varHost": lambda x: random.choice(all_users),
                "varRoom_type": lambda x: random.choice(room_types),
                "varPrice": lambda x: random.randint(10000, 100000),
                "varBaths": lambda x: random.randint(1, 5),
                "varBedrooms": lambda x: random.randint(1, 5),
                "varBeds": lambda x: random.randint(1, 5),
                "varGuests": lambda x: random.randint(1, 5),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} rooms Success"))
