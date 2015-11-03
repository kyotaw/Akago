from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.record, name='record'),
    url(r'^(?P<child_id>\d+)$', views.query, name='query'),
]
