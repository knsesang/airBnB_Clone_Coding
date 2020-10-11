from django.core.management.base import BaseCommand
from django_seed import Seed

from appRooms import models as room_models
from appUsers import models as user_models

import random

from django.contrib.admin.utils import flatten


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
        created_photos = seeder.execute()
        print(created_photos.values)  #   dict-values([[13]])
        print(list(created_photos.values()))  #   [[13]]

        created_clean = flatten(list(created_photos.values()))
        print(created_clean)  #   [13]      만들어진 pk값

        for pk in created_clean:
            room = room_models.clsRoom.objects.get(pk=pk)

            #   한 방에 여러개의 사진을 넣고 싶을때
            #   최소 1~3개의 사진을 가지게 된다ㄴ
            for i in range(1, random.randint(2, 4)):
                room_models.clsPhoto.objects.create(
                    varCaption=seeder.faker.sentence(),
                    varRoom=room,
                    varFile=f"room_photos/{random.randint(1, 50)}.jpg",
                )

        self.stdout.write(self.style.SUCCESS(f"{numbers} rooms Success"))
