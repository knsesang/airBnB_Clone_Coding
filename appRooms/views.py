from django.views.generic import ListView, DetailView
from django.utils import timezone
from . import models

#   def 함수 사용시 필요
from django.shortcuts import render, redirect

#   from django.urls import reverse

from django.http import Http404

from django_countries import countries


#   class list view 형식 페이징
#   찾는 파일은 templates/앱이름/클래스이름_list.html 을 자동으로 읽어들임
#   templates/appRooms/clsroom_list.html
#   파이썬과 장고가 합쳐진 방식
class clsHomeView(ListView):
    model = models.clsRoom
    paginate_by = 10
    paginate_orphans = 5
    ordering = "colCreated"
    context_object_name = "objRooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


#   templates/appRooms/clsroom_detail.html
class clsHomeDetail(DetailView):
    model = models.clsRoom


#   함수기반
def fn_Room_Detail(request, pk):
    #   print(pk)
    #   294

    try:
        room = models.clsRoom.objects.get(pk=pk)

        #   print(room)
        #   USNS Olsen  FPO AE 76368

        return render(
            request,
            "appRooms/detail.html",
            {
                "room": room,
            },
        )

    except models.clsRoom.DoesNotExist:
        #   return redirect("/")

        #   from django.urls import reverse 필요
        #   return redirect(reverse("appCore:home"))

        #   from django.http import Http404 필요
        #   settigs.py  에서 debug=false 일때만 확인이 가능
        raise Http404()


#   검색
def fn_Search(request):
    # print(request)
    #   <WSGIRequest: GET '/rooms/search/'>
    #   print(dir(request))

    varCity = request.GET.get("txtCity")
    #   print(varCity)
    #   varCity = str.capitalize(city)  #   니코 강의 내용
    varCity = varCity.capitalize()  #   DB 데이타는  대문자로 시작하므로

    arrRoom_types = models.clsRoomType.objects.all()
    print(arrRoom_types)
    #   <QuerySet [<clsRoomType: Apartment>, <clsRoomType: Bed and breakfast>,...>

    return render(
        request,
        "appRooms/search.html",
        {
            "varCity": varCity,
            "countries": countries,
            "arrRoom_types": arrRoom_types,
        },
    )
