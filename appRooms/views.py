from django.shortcuts import render
from . import models

#   Paginator 용
from django.core.paginator import Paginator

#   Paginator 용 함수, Paginator 는 list 가 필요하다
def fn_All_Rooms(request):

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

    #   만약 값이 없는 키가 온다면 값은 None 으로 나타난다
    #   print(request.GET.get("page"))
    #   None

    #   print(dir(request.GET.keys()))
    #   ['__and__', '__class__', '__contains__', .....]

    #   값이 없다면 1로 보이기
    varPage = request.GET.get("txtPage", 1)
    varPage = int(varPage or 1)
    #   print(varPage)

    #   전체 데이타
    arrAllRooms = models.clsRoom.objects.all()

    #   print(arrAllRooms)
    # <QuerySet [<clsRoom: 89006 Douglas Station Suite 210
    # Williamsberg, RI 66813>, <clsRoom: 37587 Powell Loaf Apt. 001
    # Barbaraport, ND 65116>, <clsRoom: 4622 Melton Ford...?>

    arrPaginator = Paginator(arrAllRooms, 10)
    arrRooms = arrPaginator.get_page(varPage)

    #   10 개 데이타
    #   print(vars(arrRooms))
    #   {'object_list': <QuerySet [<clsRoom: 89006 Douglas Station Suite 210
    #   Williamsberg, RI 66813>,...>, '...(remaining elements truncated)...']>,
    #   'per_page': 10, 'orphans': 0, 'allow_empty_first_page': True, 'count': 60, 'num_pages': 6}

    return render(
        request,
        "appRooms/home.html",
        context={
            "arrRooms": arrRooms,
        },
    )
