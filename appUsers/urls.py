from django.urls import path
from . import views

app_name = "appUsers"

urlpatterns = [
    path("login/", views.clsLoginView.as_view(), name="login"),
]
