from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'apps.core.views.home', name='home'),
    url(r'^', include('apps.core.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^users/login/', "django.contrib.auth.views.login", dict(template_name="login.html"), name="login"),
    url(r'^users/logout/', "django.contrib.auth.views.logout", {"next_page": "/"}, name="logout"),

    # -------- ADMIN -----------
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )