from django.conf.urls.defaults import *
from gholam import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^check/$', views.loginCheck),
    (r'^logic/$', views.logic),
    # Example:
    # (r'^gholam/', include('gholam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
