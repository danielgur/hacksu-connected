from django.conf.urls import patterns, include, url
from django.contrib import admin
from connected import views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connected.views.home', name='home'),
    # url(r'^connected/', include('connected.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'app_connected.views.LoginRequest'),
    (r'^loop/(\d+)/$', views.loop),
    (r'^menu/$', views.menu),
    (r'^bump/$', views.bump),
    (r'^myinfo/(\d+)/$', views.myinfo),
    (r'^register/$', 'app_connected.views.MemberRegistration'),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
