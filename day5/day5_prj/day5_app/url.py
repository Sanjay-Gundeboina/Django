from django.urls import path
from . import views
urlpatterns=[
    path("wish/",view=views.wish),
    path("user_data/",view=views.handle_user_login_data),
    # path("user/", view=views.handle_user_login_json_data)
]