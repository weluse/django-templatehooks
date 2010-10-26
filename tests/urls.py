from django.conf.urls.defaults import *


urlpatterns = patterns(
    '',
    url(r'^$', 'base.views.index'),
    url(r'^/ctx$', 'base.views.with_context'),
)
