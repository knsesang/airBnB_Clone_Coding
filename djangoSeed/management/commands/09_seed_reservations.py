import random

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from appUsers import models as user_models
from appReservations import models as reservation_models
from appRooms import models as room_models
from datetime import datetime, timedelta

from django.utils import timezone


NAME = "Conversations"


class Command(BaseCommand):
    help = "this command creates conversations"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many time?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        users = user_models.clsUser.objects.all()
        rooms = room_models.clsRoom.objects.all()

        seeder.add_entity(
            reservation_models.clsReservation,
            numbers,
            {
                "colStatus": lambda x: random.choice(
                    [
                        "pending",
                        "confirmed",
                        "canceled",
                    ]
                ),
                "colGuest": lambda x: random.choice(users),
                "colRoom": lambda x: random.choice(rooms),
                #   "colCheck_in": lambda x: datetime.now(),    #   미국시간 불러오는 문제가 있음
                "colCheck_in": lambda x: timezone.localtime(),
                #   체크 아웃 예약일은 3~25 일 이후로 잡음
                #   "colCheck_out": lambda x: datetime.now()            #   미국시간 불러오는 문제가 있음
                "colCheck_out": lambda x: timezone.localtime()
                + timedelta(days=random.randint(3, 25)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} created"))