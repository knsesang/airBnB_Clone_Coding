from django.core.management.base import BaseCommand

#   실행방법
#   python3  manage.py loveyou --times 5


class Command(BaseCommand):
    help = "This command tells me that he loves me"
    print(help)

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="how many times?",
        )

    def handle(self, *args, **options):
        times = options.get("times")

        for t in range(0, int(times)):
            #   self.stdout.write(self.style.WARNING("i love you"))     #   노랑색 글자
            self.stdout.write(self.style.SUCCESS("i love you"))  #   연두색 글자

        #   print(args, options)
