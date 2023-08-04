from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path(
        'adicionar_cliente/',
        views.adicionar_cliente,
        name='adicionar_cliente'
    ),
    path(
        'lista_clientes/',
        views.lista_clientes,
        name='lista_clientes'
    ),
    path(
        'editar_cliente/<int:id>/',
        views.editar_cliente,
        name='editar_cliente'
    ),
]
