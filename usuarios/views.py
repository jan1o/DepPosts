from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

class UsuarioCreate(CreateView):
    template_name = "signin.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        url = super().form_valid(form)

        self.object.save()

        Usuario.objects.create(user=self.object)

        return url

class UsuarioUpdate(UpdateView):
    template_name = "update.html"
    model = Usuario
    fields = ["nome", "revista"]
    success_url = reverse_lazy('hello')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Usuario, user=self.request.user)
        return self.object



