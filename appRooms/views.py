import types
from django.shortcuts import render

from datetime import datetime
from . import models

# Create your views here.
def fn_All_Rooms(request):

    now = datetime.now()

    #   from django.http import HttpResponse
    #   return HttpResponse(context=f"{now} hello")

    #   print(request)
    #   <WSGIRequest: GET '/'>

    #   print(vars(request))
    #   {'environ': {'HOSTNAME': 'docker_aairBnB', 'SHLVL': '1', ....

    #   print(dir(request))
    #   ['COOKIES', 'FILES', 'GET', 'META', 'POST', ...

    #   print(request.GET)
    #   <QueryDict: {'page': ['2'], 'city': ['seoul']}>

    #   print(vars(request.GET))
    #   {'_encoding': 'utf-8', '_mutable': False}

    #   print(dir(request.GET))
    #   ['__class__', '__contains__', '__copy__'......]

    #   print(request.GET.keys())
    #   dict_keys(['page', 'city'])

    #   print(request.GET.get("page"))
    #   2

    #   만약 값이 없는 키가 온다면 값은 Noneㄴ 으로 나타난다
    #   print(request.GET.get("page"))
    #   None

    #   print(dir(request.GET.keys()))
    #   ['__and__', '__class__', '__contains__', .....]

    #   값이 없다면 1으로 보이기

    varPage = int(request.GET.get("txtPage", 1))
    varPage_size = 10
    varLimit = varPage_size * varPage
    varOffset = varLimit - varPage_size

    #   [:5] 불러오는 갯수를 5개로 제한한다
    all_rooms = models.clsRoom.objects.all()[varOffset:varLimit]

    #   11 ~ 20 번까지 불러온다
    #   all_rooms = models.clsRoom.objects.all()[10:20]

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
