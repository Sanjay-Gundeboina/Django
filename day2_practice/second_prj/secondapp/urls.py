from django.urls import path
from . import views

urlpatterns=[
    path('second/',view=views.second)
]