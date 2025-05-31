from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:num>", views.unit, name="unit"), 
    path("unit.css", views.check, name="check") # just for debugging fml
]