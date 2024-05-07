# parkingApi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("parkings/", views.parking_list),
    path("parkings/<int:pk>/", views.parking_detail),
]
