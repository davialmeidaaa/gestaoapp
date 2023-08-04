from django.shortcuts import render, redirect
from rotulos.forms import RotuloForm


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
    
    return render(request, 'rotulos/listar_rotulo.html')