from django.shortcuts import render, redirect
from rotulos.forms import RotuloForm
from rotulos.models import Rotulo


def adicionar_rotulo(request):
    if request.method == "POST":
        form = RotuloForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('nomedaurlpararedirecionar')
        else:
            print(form.errors) # imprime os erros de validação
    else:
        form = RotuloForm()

    context = {
        'form': form,
    }
    
    return render(request, 'rotulos/adicionar_rotulo.html', context)


def listar_rotulo(request):
    
    rotulos = Rotulo.objects.all().order_by('id')
    
    for rotulo in rotulos:
        if rotulo.valor_cobrado is None:
            rotulo.valor_cobrado_formatado = "-"
        else:
            rotulo.valor_cobrado_formatado = "R$ {:,.2f}".format(rotulo.valor_cobrado).replace(",", "X").replace(".", ",").replace("X", ".")

        if rotulo.valor_recebido is None:
            rotulo.valor_recebido_formatado = "-"
        else:
            rotulo.valor_recebido_formatado = "R$ {:,.2f}".format(rotulo.valor_recebido).replace(",", "X").replace(".", ",").replace("X", ".")
        
    context = {
        'rotulos': rotulos,
    }
    
    return render(request, 'rotulos/listar_rotulo.html', context)


