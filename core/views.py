from django.shortcuts import render
from .forms import AlunoForm
from django.shortcuts import redirect
from .models import Aluno


def criar(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)  # constrói o AlunoForm com os dados que vem do formulário
        # form = AlunoForm({'nome': 'teste', 'dt_nasc': '2016-01-01', 'rg': '3355', 'endereco': 'teste', 'obs': 'teste'})
        # error = form.errors
        if form.is_valid():
            novo = form.save(commit=False)
            # dt = novo.dt_nasc
            novo.save()
            return redirect('core.views.criar')
    else:
        form = AlunoForm()
    return render(request, 'core/criar.html', {'form': form})


def listar(request):
    alunos = Aluno.objects.order_by('nome')
    return render(request, 'core/listar.html', {'alunos': alunos})



# Para mostrar um template que não tem conteúdo:
# def listar(request):
#     return render(request, 'core/listar.html', {})
