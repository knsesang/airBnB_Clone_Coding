from django.urls import path
from . import views

app_name = "appRooms"

urlpatterns = [
    #   path("<int:pk>", views.fn_Room_Detail, name="detail"),  #   함수기반
    path("<int:pk>", views.clsHomeDetail.as_view(), name="detail"),  #   함수기반
    path("search/", views.fn_Search, name="search"),
]
