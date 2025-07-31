from django.urls import path
from . import views
urlpatterns=[
    path("",view=views.wish),
    path("register_student/",view=views.register_student),
    path("update_student/<int:id>",view=views.update_student)
]
