from django.conf.urls import patterns, url
from faves import views


urlpatterns = patterns( '',
    url( r'^$', views.index, name='index' ),
    url( r'^g(?P<group_id>\d+)/$', views.group ),
    url( r'^l(?P<link_id>\d+)/', views.link),
    url( r'^l(?P<link_id>\d+)/redir/$', views.redir ),
)
