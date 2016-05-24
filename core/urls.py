from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    url(r'^core/listar/$', views.alunos_list),
    url(r'^core/criar/$', views.criar, name="criar"),
    url(r'^core/(?P<pk>[0-9]+)/edit/$', views.aluno_edit, name='aluno_edit'),
]
