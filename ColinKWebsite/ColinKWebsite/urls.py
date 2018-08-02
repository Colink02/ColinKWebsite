"""
Definition of urls for ColinKWebsite.
"""

from django.conf.urls import include, url
import Home.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', Home.views.index, name='index'),
    url(r'^home$', Home.views.index, name='home'),

    # Examples:
    # url(r'^$', ColinKWebsite.views.home, name='home'),
    # url(r'^ColinKWebsite/', include('ColinKWebsite.ColinKWebsite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
