from django.conf.urls import url
from django.contrib.staticfiles import views as staticviews

from . import views


urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^(?P<child_id>\d+)$', views.query, name='query'),
    url(r'^static/(?P<path>.*)$', staticviews.serve),
    url(r'^media/(?P<path>.*)$', staticviews.serve),
]
