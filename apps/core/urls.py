from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.core.views.home', name='core_home'),
)

