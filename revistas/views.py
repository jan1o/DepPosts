from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Revista
from .forms import RevistaForm

# Create your views here.
# @login_required
# def listarRevistaUsuario(request):
#     nome = request.GET.get('nome', None)

#     if nome and sobrenome:
#         revistas = Revista.objects.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
#     elif nome or sobrenome:
#         revistas = Revista.objects.filter(first_name__icontains=nome) | Revista.objects.filter(last_name__icontains=sobrenome)
#     else:
#         revistas = Revista.objects.all()

#     return render(request, 'lista-revista.html', {'revistas': revistas})

@login_required
def listarRevistaAdministrador(request):
    revistas = Revista.objects.all()

    return render(request, 'listar-revista.html', {'revistas': revistas})

@login_required
def adicionarRevista(request):
    form = RevistaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listarRevista')

    return render(request, 'adicionar-revista.html', {'form': form})

@login_required
def editarRevista(request, id):
    revista = get_object_or_404(Revista, pk=id)
    form = RevistaForm(request.POST or None, request.FILES or None, instance=revista)

    if form.is_valid():
        form.save()
        return redirect('listarRevista')

    return render(request, 'editar-revista.html', {'form': form})

@login_required
def excluirRevista(request, id):
    revista = get_object_or_404(Revista, pk=id)

    if request.method == 'POST':
        revista.delete()
        return redirect('listarRevista')

    return render(request, 'excluir-revista.html', {'revista': revista})
