
from django.core.management.base import BaseCommand

from appRooms.models import clsHouseRule


class Command(BaseCommand):
    help = "this command creates houserules"
    
    def handle(self, *args, **options):
        Houserules = [
            "Pets allowed",
            "Smoking allowed",
        ]

        for a in Houserules:
            print(a)
            clsHouseRule.objects.create(colName=a)
        
        self.stdout.write(self.style.SUCCESS(f"{len(Houserules)} Houserules Created"))




