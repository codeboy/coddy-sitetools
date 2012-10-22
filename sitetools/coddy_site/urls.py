# -*- coding: utf-8 -*-
"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('sitetools.coddy_site.views',
    url(r'^$', 'index', name='site_base'),

#    url(r'login/$', 'site_login', name='site_login'),
#    url(r'logout/$', 'site_logout', name='site_logout'),
)
