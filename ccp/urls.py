from django.urls import path
from .views import cadastrar_usuario, formularioParte1, formularioParte2, formularioParte3, \
                    formularioParte4, formularioParte5, formularioParte6, \
                    indexView, createView, logar_usuario, \
                    updateView, deleteView

urlpatterns = [
    path('', indexView, name='index'),

    # Formulários
    path('formulario1', formularioParte1, name='formulario1'),
    path('formulario2', formularioParte2, name='formulario2'),
    path('formulario3', formularioParte3, name='formulario3'),
    path('formulario4', formularioParte4, name='formulario4'),
    path('formulario5', formularioParte5, name='formulario5'),
    path('formulario6', formularioParte6, name='formulario6'),

    # CRUD
    path('create/', createView, name='create'),
    path('update/<int:id>/', updateView, name='update'),
    path('delete/<int:id>/', deleteView, name='delete'),

    # Login
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    # path('index', indexView, name="index"),
]
