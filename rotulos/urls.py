from django.urls import path
from . import views

app_name = 'rotulos'

urlpatterns = [
    path(
        'adicionar_rotulo/',
        views.adicionar_rotulo,
        name='adicionar_rotulo'
    ),
    path(
        'listar_rotulo/',
        views.listar_rotulo,
        name='listar_rotulo'
    ),
]