from django.core.management.base import BaseCommand
from django_seed import Seed

from appRooms import models as room_models
from appUsers import models as user_models

import random

""" 
i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
f = random()   # 0부터 1 사이의 임의의 float
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
i = randrange(10)  # 0부터 9 사이의 임의의 정수 
"""

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

        #   장된 pk 값을 반환 받아온다
        created_photos = seeder.execute()
        #   print(created_photos)
        #   <class 'rooms.models.clsRoom'>: [451, 452, 453, 454, 455, 456]}

        #   print(created_photos.values)
        #   <built-in method values of dict object at 0x7f17980fa2c0> ㅌ

        #   print(list(created_photos.values()))
        #   [[178, 179, 180, 181, 182]]

        #   flatten은 여러겹 쌓인 리스트를 하나의 리스트로 리턴한다.
        created_clean = flatten(list(created_photos.values()))
        #   print(created_clean)
        #   [178, 179]

        amenities = room_models.clsAmenity.objects.all()
        facilities = room_models.clsFacility.objects.all()
        houserules = room_models.clsHouseRule.objects.all()

        for pk in created_clean:
            room = room_models.clsRoom.objects.get(pk=pk)

            #   한 방에 여러개의 사진을 넣고 싶을때
            #   최소 1~3개의 사진을 가지게 된다
            #   random.randint(2, 4) : 2 ~ 4
            #   range(1, random.randint(2, 4)) : 1 ~ 3

            for i in range(1, random.randint(2, 4)):
                room_models.clsPhoto.objects.create(
                    varCaption=seeder.faker.sentence(),
                    varRoom=room,
                    varFile=f"room_photos/{random.randint(1, 50)}.jpg",
                )

            for a in amenities:
                magic_number = random.randint(0, len(amenities))
                if magic_number % 2 == 0:  #   짝수라면 추가
                    room.varAmenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, len(facilities))
                if magic_number % 2 == 0:
                    room.varFacilities.add(f)

            for r in houserules:
                magic_number = random.randint(0, len(houserules))
                if magic_number % 2 == 0:
                    room.varHouse_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{numbers} rooms Success"))
