from django.shortcuts import render


def criar(request):
    return render(request, 'core/criar.html', {})
