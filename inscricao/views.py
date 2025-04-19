from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pessoa
from django.core.mail import send_mail

def index(request):
    return render(request, 'inscricao/index.html')

def processa_inscricao(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    
    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    # send_mail('Assunto do email', 'Texto do e-mail.', 'enviar@email.com', recipient_list=[email,])
    
    return HttpResponse(f'Pessoa {nome}-{email} salva com sucesso!')