from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    # url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<post_slug>[-\w]+)/$', views.detail, name='detail'),
    url(r'^cat/(?P<cat_slug>[-\w]+)/$', views.list_category, name='list_category'),
]
