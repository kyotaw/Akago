from django.conf.urls import url

from django.contrib.staticfiles import views as statiicviews

from . import views


urlpatterns = [
    url(r'^static/(?P<path>.*)$', statiicviews.serve),
    url(r'^media/(?P<path>.*)$', statiicviews.serve),
]
