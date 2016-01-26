from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from blog.views import *

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url="/blog/show/")),
    url(r'^show/$', show_blog),
    url(r'^(?P<id>\d+)/$', blog_id),
    url(r'^creat/$', creat_blog),

)


