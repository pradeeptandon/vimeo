from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vimeo.views.home', name='home'),
    # url(r'^vimeo/', include('vimeo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^searching/$','userbase.views.filt'),
    url(r'^display/$','userbase.views.display'),
                       
    url(r'^pay/(\w+)/$','userbase.views.filt_pay'),
    url(r'^vid/(?P<queries>\w+)/$','userbase.views.filt_vid'),
    url(r'^sp/(?P<queries>\w+)/$','userbase.views.filt_sp'),
                       

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
    
)
