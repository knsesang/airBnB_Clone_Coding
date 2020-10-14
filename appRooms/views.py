from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.utils import timezone
from . import models
from . import forms  #   form API 사용하기 위해서

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


#   수작업 방식의 검색. 강의 ~ #13.6.
#   fn_Search() → fn_nomal_Search() 로 이름 변경
#   search.html → _search.html 로 이름 변경
def fn_normal_Search(request):
    # print(request)
    #   <WSGIRequest: GET '/rooms/search/'>
    #   print(dir(request))

    varCity = request.GET.get("txtCity", "Anywhere")
    #   print(varCity)
    #   varCity = str.capitalize(city)  #   니코 강의 내용
    varCity = varCity.capitalize()  #   DB 데이타는  대문자로 시작하므로

    #   사용자가 선택한 국가 코드
    varCountry = request.GET.get("selCountry", "KR")

    #   사용자가 선택한 room type pk
    varRoom_type = int(request.GET.get("selRoom_type", 0))
    varPrice = int(request.GET.get("txtPrice", 0))
    varGuests = int(request.GET.get("txtGuests", 0))
    varBedrooms = int(request.GET.get("txtBedrooms", 0))
    varBeds = int(request.GET.get("txtBeds", 0))
    varBaths = int(request.GET.get("txtBaths", 0))

    #   checkbox는 선택이 되면 on 으로 값이 온다
    #   값을 True / False 로 받기 위해서 bool 함수를 사용한다
    varInstant_book_only = bool(request.GET.get("chkInstant_book_only", False))
    varSuperhost_only = bool(request.GET.get("chkSuperhost_only", False))

    #   list 형식으로 받을때는 getlist
    varAmenities = request.GET.getlist("chkAmenities")
    #   print(varAmenities)
    #   ['36', '39']

    varFacilities = request.GET.getlist("chkFacilities")
    #   print(varFacilities)
    varHouse_rules = request.GET.getlist("chkHouse_rules")
    #   print(varHouse_rules)

    arrRoom_types = models.clsRoomType.objects.all()
    #   print(arrRoom_types)
    #   <QuerySet [<clsRoomType: Apartment>, <clsRoomType: Bed and breakfast>,...>

    arrAmenities = models.clsAmenity.objects.all()
    arrFacilities = models.clsFacility.objects.all()
    arrHouse_rules = models.clsHouseRule.objects.all()

    #   사용자가 선택한 web form 값들 모음
    form = {
        "varCity": varCity,
        "varCountry": varCountry,
        "varRoom_type": varRoom_type,
        "varPrice": varPrice,
        "varGuests": varGuests,
        "varBedrooms": varBedrooms,
        "varBeds": varBeds,
        "varBaths": varBaths,
        "varInstant_book_only": varInstant_book_only,
        "varSuperhost_only": varSuperhost_only,
        "varAmenities": varAmenities,
        "varFacilities": varFacilities,
        "varHouse_rules": varHouse_rules,
    }

    #   print("varCity : " + varCity)
    #   print("varCountry : " + varCountry)
    #   print(f"varRoom_type : {varRoom_type}")

    #   사용자에게 전달되는 선택해야 할 값들
    choices = {
        "countries": countries,  # 장고 국가 선택 앱
        "arrRoom_types": arrRoom_types,
        "arrAmenities": arrAmenities,
        "arrFacilities": arrFacilities,
        "arrHouse_rules": arrHouse_rules,
    }

    filter_args = {}

    if varCity != "Anywhere":
        filter_args["colCity__startswith"] = varCity

    filter_args["colCountry"] = varCountry

    if varRoom_type != 0:
        filter_args["colRoom_type__pk"] = varRoom_type

    if varPrice != 0:
        filter_args["colPrice__lte"] = varPrice

    if varGuests != 0:
        filter_args["colGuests__gte"] = varGuests

    if varBedrooms != 0:
        filter_args["colBedrooms__gte"] = varBedrooms

    if varBeds != 0:
        filter_args["colBeds__gte"] = varBeds

    if varBaths != 0:
        filter_args["colBaths__gte"] = varBaths

    if varInstant_book_only is True:
        filter_args["colInstant_book"] = True

    if varSuperhost_only is True:
        filter_args["colHost_colSuperhost"] = True

    if len(varAmenities) > 0:
        for a in varAmenities:
            filter_args["colAmenities__pk"] = int(a)

    if len(varFacilities) > 0:
        for f in varAmenities:
            filter_args["colFacilities__pk"] = int(f)

    if len(varHouse_rules) > 0:
        for h in varHouse_rules:
            filter_args["colHouse_rules__pk"] = int(h)

    arrRooms = models.clsRoom.objects.filter(**filter_args)

    #   print(filter_args)

    return render(
        request,
        "appRooms/search.html",
        {
            **form,
            **choices,
            "arrRooms": arrRooms,
        },
    )


#   검색 form API 사용
def fn_Search(request):
    form = forms.clsSearchform()

    return render(
        request,
        "appRooms/search.html",
        {
            "form": form,
        },
    )
