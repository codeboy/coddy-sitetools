#-*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SiteSettings(models.Model):
    """
    Settings for site
    """
#    site_id =

    class Meta:
        verbose_name, verbose_name_plural = _(u'Profile'), _(u'Profiles')

    def __unicode__(self):
        return self.user.username


