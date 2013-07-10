from django.conf.urls import patterns, include, url
from so.views import  loginAction
from so.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sonet.views.home', name='home'),
    # url(r'^Sonet/', include('Sonet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^hello/$',hello),
    ('^login/$',loginAction),
)
