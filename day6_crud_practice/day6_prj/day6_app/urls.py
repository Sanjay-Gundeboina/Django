from django.urls import path
from . import views

urlpatterns = [
        path("",view=views.wellcome),
        path("get_users/",view=views.get_users),
        path("post_users/",view=views.post_users),
        path("patch_users/<int:id>",view=views.patch_users),
        path("put_users/<int:id>",view=views.put_users),
        path("del_users/<int:id>",view=views.del_users)
]
