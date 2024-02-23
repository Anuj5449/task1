from django.urls import path
from .views import creat_api,details_api

urlpatterns = [
    path('add/', creat_api),
    path('show/<int:pk>/', details_api),
]
