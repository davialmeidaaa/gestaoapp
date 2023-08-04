from django.shortcuts import render, redirect
from clientes.forms import ClienteForm


def adicionar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'clientes/adicionar_cliente.html', context)


def lista_clientes(request):

    return render(request, 'clientes/listar_clientes.html')

