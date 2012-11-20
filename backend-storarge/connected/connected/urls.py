from django.conf.urls import patterns, include, url
from connected import views

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

    (r'^loop/(\d+)/$', views.loop),
    (r'^menu/$', views.menu),
    (r'^bump/$', views.bump),
    (r'^myinfo/(\d+)/$', views.myinfo),
    (r'^register/$', 'views.MemberRegistration'),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
