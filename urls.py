from django.conf.urls.defaults import *
from django.conf import settings
from gholam import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^logic/$', views.logic),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )