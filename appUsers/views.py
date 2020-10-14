from django.shortcuts import render

#   clsSearchView 를 위해서 추가
#   from django.views.generic import View   도 실행가능
from django.views import View

from django.shortcuts import render


class clsLoginView(View):
    def get(self, request):
        return render(
            request,
            "appUsers/login.html",
        )

    def post(self, request):
        pass
