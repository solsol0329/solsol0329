from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.readcsv),
    path('process/', views.process),
    path('avg/', views.avg),
]
