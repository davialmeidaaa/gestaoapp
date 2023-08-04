from django.shortcuts import render, redirect, get_object_or_404
from clientes.forms import ClienteForm
from clientes.models import Cliente


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
    
    clientes = Cliente.objects.all().order_by('id')
    
    context = {
        'clientes': clientes,
    }

    return render(request, 'clientes/listar_clientes.html', context)


def editar_cliente(request, id):
    
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('clientes:lista_clientes')

    context = {
        'form': form,
        'cliente': cliente
    }

    return render(request, 'clientes/adicionar_cliente.html', context)
