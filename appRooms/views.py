from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

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

    hungry = True

    return render(
        request,
        "all_rooms.html",
        context={"now": now, "hungry": hungry},
    )
