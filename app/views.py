from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def sobre(request):
    return render(request, 'sobre.html')

def doacoes(request):
    return render(request, 'doacoes.html')

def adocao(request):
    return render(request, 'adocao.html')
