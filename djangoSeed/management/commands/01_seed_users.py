from django.core.management.base import BaseCommand
from django_seed import Seed
from appUsers import models as user_models
import random


class Command(BaseCommand):
    help = "this command creates users"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many ?")

    def handle(self, *args, **options):

        numbers = options.get("numbers")

        arrLanguage = (
            "kor",
            "eng",
            "other",
        )

        arrGender = (
            "male",
            "female",
            "other",
        )

        arrCurrency = (
            "usd",
            "krw",
            "other",
        )

        seeder = Seed.seeder()

        #   superhost,superuser, staff 는 만들지 않을예정
        seeder.add_entity(
            user_models.clsUser,
            numbers,
            {
                "colGender": lambda x: random.choice(arrGender),
                "colLanguage": lambda x: random.choice(arrLanguage),
                "colCurrency": lambda x: random.choice(arrCurrency),
                "colSuperhost": False,
                "is_staff": False,
                "is_superuser": False,
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} users created"))