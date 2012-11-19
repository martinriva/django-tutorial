from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.blog.views.home', name='blog_home'),
    url(r'^posts/?$', 'apps.blog.views.posts', name='blog_posts'),
    url(r'^post/create/$', 'apps.blog.views.create_post', name='blog_create_post'),
    url(r'^post/edit/(?P<post_id>\d+)/$', 'apps.blog.views.edit_post', name='blog_edit_post'),
    url(r'^post/comment/$', 'apps.blog.views.comment_post', name='blog_comment_post'),    
)