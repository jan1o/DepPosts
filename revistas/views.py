from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from .models import Revista
from .forms import RevistaForm


class ListRevistas(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Revista
    template_name = 'listar-revista.html'

class CreateRevista(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "adicionar-revista.html"
    form_class = RevistaForm
    success_url = reverse_lazy('list_revistas')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UpdateRevista(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Revista
    fields = ['nome']
    template_name = "editar-revista.html"
    success_url = reverse_lazy('list_revistas')

class DeleteRevista(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Revista
    template_name = "excluir-revista.html"
    success_url = reverse_lazy('list_revistas')
