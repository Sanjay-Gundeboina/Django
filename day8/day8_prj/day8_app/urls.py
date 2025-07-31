from django.urls import path
from . import views
urlpatterns=[
    path("",view=views.welcome),
    path("reg_user/",view=views.reg_user),
    path("get_user/<int:id>",view=views.get_user),
    path("update_emp/<int:emp_id>",view=views.update_emp)
]