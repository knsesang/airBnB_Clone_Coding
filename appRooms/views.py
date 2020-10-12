from django.views.generic import ListView
from django.utils import timezone
from . import models

#   def 함수 사용시 필요
from django.shortcuts import render

#   class list view 형식 페이징
#   찾는 파일은 templates/앱이름/클래스이름_list.html 을 자동으로 읽어들임
#   templates/appRooms/clsroom_list.html
#   파이썬과 장고가 합쳐진 방식
class clsHomeview(ListView):
    model = models.clsRoom
    paginate_by = 10
    paginate_orphans = 5
    ordering = "varCreated"
    context_object_name = "objRooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def fn_Room_Detail(request, pk):
    print(pk)

    return render(
        request,
        "appRooms/detail.html",
    )
