from django.urls import path
from . import views

urlpatterns = [
    path("third/",view=views.third),
    path("user_login/",view=views.user_login)
]
