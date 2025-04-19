from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pessoa

def index(request):
    return render(request, 'inscricao/index.html')

def processa_inscricao(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    
    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    
    return HttpResponse(f'Pessoa {nome}-{email} salva com sucesso!')