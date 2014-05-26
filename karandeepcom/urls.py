from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('thebigsmallgif.urls')),
	url(r'^thebigsmallgif/', include('thebigsmallgif.urls')),
    # Examples:
    # url(r'^$', 'karandeepcom.views.home', name='home'),
    #url(r'^karandeepcom/', include('karandeepcom.foo.urls')),
    #url(r'^thebigsmallgif/', include('thebigsmallgif.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
