from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info_estudiante/', views.info_estudiante, name='info_estudiante'),
]