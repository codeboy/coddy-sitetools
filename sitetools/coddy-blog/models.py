#-*- coding: utf-8 -*-
import datetime

from django.db import models as m
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User



class Post(m.Model):
    """
    blog posts
    """
    author = m.ForeignKey(User,
        verbose_name=_('Author'),)

    title = m.CharField(
        max_length=225,
        verbose_name=_('Title'),
        help_text=_('post title'),
        unique=True,)
    title_slug = m.SlugField(
        max_length=250,
        unique=True,
        verbose_name=_('title slug'),
        help_text=_('slug for URL'),)

    description = m.TextField(
        null=True, blank=True,
        verbose_name=_('Description'),
        help_text=_('description or preview of post'),)
#    logo = m.CharField(
#        max_length=100,
#        verbose_name=_('Project logo'),
#        default='ballon.png',
#    )

    content = m.TextField(
        null=False, blank=False,
        verbose_name=_('Content of post'),
    )

    datetime_created = m.DateTimeField(
        default=datetime.datetime.now,
        verbose_name=_('Created daytime'),)
    datetime_modifed = m.DateTimeField(
        default=datetime.datetime.now,
        verbose_name=_('Modify datime'),)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Post'), _(u'Posts')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.datetime_modifed = datetime.datetime.now()
        if self.title_slug is None:
            self.title_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Tag(m.Model):
    name = m.CharField(
        max_length=225,
        verbose_name=_('name'),
        help_text=_('tag name'),
        unique=True,)
    name_slug = m.SlugField(
        max_length=250,
        unique=True,
        verbose_name=_('name slug'),
        help_text=_('slug for URL'),)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Tag'), _(u'Tags')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

