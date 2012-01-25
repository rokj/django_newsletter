from django.conf.urls.defaults import patterns, include, url

from newsletter import views as newsletter_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # newsletter
    (r'^newsletter/subscribe/$', newsletter_views.try_to_subscribe),
    (r'^newsletter/unsubscribe/$', newsletter_views.try_to_unsubscribe),
    (r'^newsletter/subscribe/key=(?P<key>[\w]+)$', newsletter_views.subscribe, { 'subscribed': True }),
    (r'^newsletter/unsubscribe/key=(?P<key>[\w]+)$', newsletter_views.subscribe, { 'subscribed': False }),
)
