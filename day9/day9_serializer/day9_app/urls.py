from django.urls import path
from . import views

urlpatterns=[
    path("",view=views.hello),
    path("get_users/",view=views.get_users),
    path("get_user_id/<int:id>",view=views.get_user_id),
    path("del_user/<int:id>",view=views.del_user)
]