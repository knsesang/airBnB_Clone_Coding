from django.urls import path
from appRooms import views as room_views

app_name = "appCore"

urlpatterns = [
    #   path("", room_views.fn_All_Rooms, name="home"),     #   paginator 이용할때
    path("", room_views.clsHomeView.as_view(), name="home"),  #   paginator 이용할때
]
