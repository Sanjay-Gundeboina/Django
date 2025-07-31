from django.urls import path
from . import views

urlpatterns=[
    path("welcome/",view=views.welcome),
    path("get_users/",view=views.get_users),
    path("post_users/",view=views.post_users),
    path("patch_users/<int:id>",view=views.patch_users)
]