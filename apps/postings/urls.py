from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^page$', views.post_page),
    url(r'^postmessage/(?P<id>\d+)$', views.process),
    url(r'^allposts/(?P<user_name>\w+)$', views.allposts),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]