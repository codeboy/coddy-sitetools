# -*- coding: utf-8 -*-

""" Default urlconf for c300 """
from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

def bad(request):
    """ Simulates a server error """
    1 / 0



urlpatterns = patterns('',
    (r'', include('sitetools.coddy_site.urls', namespace='site')),
    (r'^card/', include('sitetools.cardgame.urls', namespace='card')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^', include('debug_toolbar_user_panel.urls')),
    url(r'^bad/$', bad, name='test2'),

)




## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
