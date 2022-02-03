from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from .models import Revista
from .forms import RevistaForm


class ListRevistas(ListView):
    model = Revista
    template_name = 'listar-revista.html'

class CreateRevista(CreateView):
    template_name = "adicionar-revista.html"
    form_class = RevistaForm
    success_url = reverse_lazy('list_revistas')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UpdateRevista(UpdateView):
    model = Revista
    fields = ['nome']
    template_name = "editar-revista.html"
    success_url = reverse_lazy('list_revistas')

class DeleteRevista(DeleteView):
    model = Revista
    template_name = "excluir-revista.html"
    success_url = reverse_lazy('list_revistas')

'''
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
'''