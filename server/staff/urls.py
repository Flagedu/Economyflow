from django.urls import path, include

from .views import *

app_name = "staff"


urlpatterns = [
    path("logout/", logout_request, name="logout"),
    path("login/", Login.as_view(), name="login"),
    path("", Dashboard.as_view(), name="dashboard"),
    path("users/", AllUser.as_view(), name="all_user"),
]
