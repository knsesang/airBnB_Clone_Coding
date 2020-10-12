from django.urls import path
from . import views

app_name = "appRooms"

urlpatterns = [
    path("<int:pk>", views.fn_Room_Detail, name="detail"),
]
