from django.conf.urls import url
from . import views

#urlpatterns = [
#    url(r'^$', views.listar_articulo),
#    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
#    url(r'^post/new/$', views.postear_nuevo, name='postear_nuevo'),
#    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_articulo, name='editar_articulo'),
#]
#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.iniciar),
    url(r'^administrador$', views.administrador),
    url(r'^new/$', views.post_detailboleta),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.editar_boleta),
    url(r'^$', views.listar_boleta),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.eliminar_boleta),
    url(r'^new/$', views.post_detailcurso),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.editar_curso),
    url(r'^$', views.listar_curso),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.eliminar_curso),
    url(r'^new/$', views.post_detailusuario),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.editar_usuario),
    url(r'^$', views.listar_usuarios),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.eliminar_usuario),
    url(r'^$', views.listar_boleta_usuario),
    url(r'^usuario$', views.usuario),
    url(r'^salir$', views.salir),
    url(r'^new/$', views.post_detailalumno),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.editar_alumno),
    url(r'^$', views.listar_alumnos),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.eliminar_alumnos),
]
