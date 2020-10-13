from django.core.management.base import BaseCommand

#   Amenity 만 임포트할때
from appRooms.models import clsFacility


class Command(BaseCommand):
    help = "this command creates facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", default=1, type=int, help="how many?")

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            print(f)
            clsFacility.objects.create(colName=f)

        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created"))
