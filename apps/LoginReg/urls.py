from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.reg),
    url(r'^good$', views.good),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update)
]