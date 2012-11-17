from django.conf.urls import patterns, include, url
from app_connected.api import MemberResource


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

member_resource = MemberResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connected.views.home', name='home'),
    # url(r'^connected/', include('connected.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # api
    (r'^api/', include(member_resource.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
