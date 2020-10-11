from django.urls import path
from appRooms import views as room_views

app_name = "appCore"

urlpatterns = [
    path("", room_views.fn_All_Rooms, name="home"),
]
