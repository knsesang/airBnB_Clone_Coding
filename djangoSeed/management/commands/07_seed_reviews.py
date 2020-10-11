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
                "varAccuracy": lambda x: random.randint(1, 5),
                "varCommunication": lambda x: random.randint(1, 5),
                "varCleanliness": lambda x: random.randint(1, 5),
                "varLocation": lambda x: random.randint(1, 5),
                "varCheck_in": lambda x: random.randint(1, 5),
                "varValue": lambda x: random.randint(1, 5),
                "varRoom": lambda x: random.choice(rooms),
                "varUser": lambda x: random.choice(users),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} reviews created"))