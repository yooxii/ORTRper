from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkouts", views.checkouts, name="checkouts"),
]