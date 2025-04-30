from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processa_inscricao', views.processar_inscricao, name='processa_inscricao')
]