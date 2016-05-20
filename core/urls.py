from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    url(r'^core/listar/$', views.listar),
    url(r'^core/criar/$', views.criar, name="criar"),
]
