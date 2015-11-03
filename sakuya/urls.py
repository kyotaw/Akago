"""sakuya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r"/", 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/login.html'}),
    url(r'^timeline/', include('sakuya.timeline.urls', namespace='timeline')),
    url(r'^dashboard/', include('sakuya.dashboard.urls', namespace='dashboard')),
    url(r'^photos/', include('sakuya.photos.urls', namespace='photos')),
    url(r'^strength/', include('sakuya.strength.urls', namespace='strength')),
    url(r'^voice/', include('sakuya.voice.urls', namespace='voice')),
    url(r'^vocaburary/', include('sakuya.vocaburary.urls', namespace='vocaburary')),
    url(r'^motions/', include('sakuya.motions.urls', namespace='motions')),
]
