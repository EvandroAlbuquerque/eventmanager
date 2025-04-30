from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pessoa
# from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw
from hashlib import sha256

def index(request):
    return render(request, 'inscricao/index.html')

def processar_inscricao(request):
    
    def criar_convite(nome, email):
        template_convite = os.path.join(settings.STATIC_ROOT, 'img/yellow-ticket.png')
        img = Image.open(template_convite)
        img_escrita = ImageDraw.Draw(img)
        img_escrita.text((1300,2800), nome, fill=(0,0,0), font_size=200, stroke_width=5)
        img_escrita.text((1300,3000), email, fill=(0,0,0), font_size=150)
        chave = 'appDJANGOcelery'
        string = email+chave
        hash = sha256(string.encode()).hexdigest()
        url_convite = f'convites/{hash}.png'
        salvar_convite = os.path.join(settings.MEDIA_ROOT, f'convites/{hash}.png')
        img.save(salvar_convite)
        
        return settings.MEDIA_URL + url_convite
        
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    fonte_convite = criar_convite(nome, email)
    # send_mail('Assunto do email', 'Texto do e-mail.', 'enviar@email.com', recipient_list=[email,])
    
    return render(request, 'inscricao/confirmacao_cadastro.html', {'src_convite': fonte_convite})