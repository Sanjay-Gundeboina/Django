from django.urls import path
from . import views

urlpatterns = [
    path("wish/",view=views.wish),
    path("get/",view=views.get_api),
    path("post/",view=views.post_api),
    path("put/",view=views.put_api),
    path("patch/",views.patch_api),
    path("delete/",view=views.del_api)
]
