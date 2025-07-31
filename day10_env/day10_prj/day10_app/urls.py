from django.urls import path
from . import views
urlpatterns = [
    path("",view=views.welcome),
    path("create_cars/",view=views.create_cars),
    path("get_cars/<int:id>",view=views.get_cars),
    path("update_car/<int:id>",view=views.update_car),
    path("delete_car/<int:id>",view=views.delete_car)
]
