from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processa_inscricao', views.processa_inscricao, name='processa_inscricao')
]