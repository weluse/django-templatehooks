from django.conf.urls.defaults import *


urlpatterns = patterns(
    '',
    url(r'^$', 'base.views.index'),
)
