from django.conf.urls import url
from django.contrib.staticfiles import views as statiicviews

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)$', statiicviews.serve),
    url(r'^media/(?P<path>.*)$', statiicviews.serve),
]
