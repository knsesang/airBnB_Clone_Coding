from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from . import models

# Create your views here.
def fn_All_Rooms(request):
    #   print(request)
    #   <WSGIRequest: GET '/'>

    #   print(vars(request))
    #   {'environ': {'HOSTNAME': 'docker_aairBnB', 'SHLVL': '1', ....

    #   print(dir(request))
    #   ['COOKIES', 'FILES', 'GET', 'META', 'POST', ...

    now = datetime.now()
    #   return HttpResponse(context=f"{now} hello")

    all_rooms = models.clsRoom.objects.all()
    # print(all_rooms)
    # <QuerySet [<clsRoom: 89006 Douglas Station Suite 210
    # Williamsberg, RI 66813>, <clsRoom: 37587 Powell Loaf Apt. 001
    # Barbaraport, ND 65116>, <clsRoom: 4622 Melton Ford...?>

    return render(
        request,
        #   "all_rooms.html",
        "rooms/home.html",
        context={
            "now": now,
            "potato": all_rooms,
        },
    )
