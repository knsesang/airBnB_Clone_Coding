from django.core.management.base import BaseCommand

from appRooms.models import clsRoomType


class Command(BaseCommand):
    help = "this command creates roomtype"

    def handle(self, *args, **options):
        RoomTypes = [
            "House",
            "Apartment",
            "Bed and breakfast",
            "Boutique hotel",
            "Bungalow",
            "Cabin",
            "Chalet",
            "Cottage",
            "Guest suite",
            "Guesthouse",
            "Hostel",
            "Hotel",
            "Loft",
            "Resort",
            "Serviced apartment",
            "Townhouse",
            "Villa",
        ]

        for a in RoomTypes:
            print(a)
            clsRoomType.objects.create(colName=a)

        self.stdout.write(self.style.SUCCESS(f"{len(RoomTypes)} RoomTypes Created"))
