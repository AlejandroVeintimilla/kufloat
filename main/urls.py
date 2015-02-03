from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webkufloat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^inicio/$', views.inicio, name='inicio'),

    url(r'^quienes_somos/$', views.quienes_somos, name='quienes_somos'),
    url(r'^sesion_flotacion/$', views.sesion_flotacion, name='sesion_flotacion'),
    url(r'^programas/$', views.programas, name='programas'),
    url(r'^programa/$', views.programa, name='programa'),

    url(r'^vacio_baneficios/$', views.vacio_baneficios, name='vacio_baneficios'),
    url(r'^historia_actualidad/$', views.historia_actualidad, name='historia_actualidad'),
    url(r'^efectos_explicacion/$', views.efectos_explicacion, name='efectos_explicacion'),
    url(r'^investigacion_cientifica/$', views.investigacion_cientifica, name='investigacion_cientifica'),

    url(r'^contacto/$', views.contacto, name='contacto')
)
