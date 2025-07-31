from django.urls import path
from . import views
urlpatterns = [
    path('first/',view=views.first)
]
