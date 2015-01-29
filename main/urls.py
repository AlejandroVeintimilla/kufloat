from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webkufloat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^inicio/$', views.inicio, name='inicio'),
    
    url(r'^quienes_somos/$', views.quienes_somos, name='quienes_somos'),
    url(r'^sesion_flotacion/$', views.sesion_flotacion, name='sesion_flotacion'),
    url(r'^programas/$', views.programas, name='programas'),
    
    url(r'^historia_actualidad/$', views.historia_actualidad, name='historia_actualidad'),
    url(r'^efectos_explicacion/$', views.efectos_explicacion, name='efectos_explicacion'),
    url(r'^e_explicacion/$', views.e_explicacion, name='e_explicacion'),
    
    url(r'^contacto/$', views.contacto, name='contacto')
)
