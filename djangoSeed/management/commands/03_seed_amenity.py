from django.core.management.base import BaseCommand

#   Amenity 만 임포트할때
from appRooms.models import clsAmenity


class Command(BaseCommand):
    help = "this command creates amenities"

    #   갯수를 안 받으므로 주석처리한다
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many?",
    #     )

    def handle(self, *args, **options):
        Amenities = (
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        )

        for a in Amenities:
            print(a)
            clsAmenity.objects.create(colName=a)

        self.stdout.write(self.style.SUCCESS(f"{len(Amenities)} Amenities Created"))
