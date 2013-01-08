# -*- coding: utf-8 -*-
"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns
from django.views.generic.base import TemplateView
from views import *


urlpatterns = patterns('sitetools.cardgame.views',
#    url(r'^$', 'index', name='site_base'),

#    url(r'login/$', 'site_login', name='site_login'),
#    url(r'logout/$', 'site_logout', name='site_logout'),

#    url(r'^login/$', LoginView.as_view(), name='login'),
#    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'deck/$', DeckView.as_view(), name='deck-view'),
)
