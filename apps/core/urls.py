from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.core.views',
    url(r'^$', 'home', name='core_home'),
    #url(r'^example/', 'example', name="core_example"),
)

