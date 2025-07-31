from django.urls import path
from . import views
urlpatterns = [
    path("wish/",view=views.wish),
    path("get_users/",view=views.get_users)
]
