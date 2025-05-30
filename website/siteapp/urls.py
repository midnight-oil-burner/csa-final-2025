from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:num>",views.unit, name="unit") 
]