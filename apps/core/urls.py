from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^home/$', 'apps.core.views.home', name='core_home'),    
    url(r'^posts/$', 'apps.core.views.posts', name='core_posts'),
)
