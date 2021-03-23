from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

"""
def cadastrar_usuario(request):
    form = usuario_form(request.POST, None)
    if form.is_valid():
        form.save();
    return render(request, 'usuario_form.html', {'form': form})
"""

def cadastrar_usuario(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'Usuario cadastrado com sucesso!')
    return render(request, 'usuario_form.html',{'form':form})


