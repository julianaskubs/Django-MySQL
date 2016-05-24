from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import AlunoForm
from django.shortcuts import redirect
from .models import Aluno
from django.core.paginator import Paginator
from django.template import RequestContext


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


def alunos_list(request):
    alunos_lst = Aluno.objects.all().order_by('nome')
    paginator = Paginator(alunos_lst, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        alunos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        alunos = paginator.page(paginator.num_pages)

    return render_to_response('core/listarall.html',
                              {'alunos': alunos},
                              context_instance=RequestContext(request))


def aluno_edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            upd = form.save(commit=False)
            upd.save()
        return redirect('core.views.alunos_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'core/edit.html', {'form': form})


# Para mostrar um template que não tem conteúdo:
# def listar(request):
#     return render(request, 'core/listar.html', {})
