from django.core.management.base import BaseCommand
from django_seed import Seed
from appUsers import models as user_models
from appReviews import models as review_models
from appRooms import models as room_models

import random


class Command(BaseCommand):
    help = "this command creates review"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many ?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        users = user_models.clsUser.objects.all()
        rooms = room_models.clsRoom.objects.all()
        seeder.add_entity(
            review_models.clsReview,
            numbers,
            {
                "colAccuracy": lambda x: random.randint(1, 5),
                "colCommunication": lambda x: random.randint(1, 5),
                "colCleanliness": lambda x: random.randint(1, 5),
                "colLocation": lambda x: random.randint(1, 5),
                "colCheck_in": lambda x: random.randint(1, 5),
                "colValue": lambda x: random.randint(1, 5),
                "colRoom": lambda x: random.choice(rooms),
                "colUser": lambda x: random.choice(users),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} reviews created"))