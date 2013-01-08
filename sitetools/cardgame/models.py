#-*- coding: utf-8 -*-

import datetime

from django.db import models as m
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User

#from django.utils.translation import ugettext_lazy as _
from sitetools.coddy_site.utils import lang_stub as _




class CardProject(m.Model):
    """    card line    """

    name = m.CharField(max_length=225, unique=True, verbose_name=_('project name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'))

    class Meta:
        verbose_name, verbose_name_plural = _(u'Project'), _(u'Projects')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(CardProject, self).save(*args, **kwargs)



class CardRelease(m.Model):
    """    card release    """

    name = m.CharField(max_length=225, unique=True, verbose_name=_('project name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'))
    card_project = m.ForeignKey(CardProject)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Release'), _(u'Releases')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(CardRelease, self).save(*args, **kwargs)



class CardType(m.Model):
    """    card type    """

    name = m.CharField(max_length=225, unique=True, verbose_name=_('project name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'))
    abbr = m.CharField(max_length=3)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Type'), _(u'Types')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(CardType, self).save(*args, **kwargs)



class CardAttribute(m.Model):
    """    card type    """

    name = m.CharField(max_length=225, unique=True, verbose_name=_('project name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'))
    abbr = m.CharField(max_length=3)
    value = m.CharField(max_length=12, blank=True, null=True, verbose_name=_('10 digit + 2'))

    class Meta:
        verbose_name, verbose_name_plural = _(u'Attribute'), _(u'Attributes')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(CardAttribute, self).save(*args, **kwargs)


class CardColor(m.Model):
    """    card type    """

    name = m.CharField(max_length=225, unique=True, verbose_name=_('project name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'))
    abbr = m.CharField(max_length=3)


    class Meta:
        verbose_name, verbose_name_plural = _(u'Color'), _(u'Colors')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(CardColor, self).save(*args, **kwargs)


class Card(m.Model):
    """
    card
    """
    CHOICES_RARITY = (('CMN', 'common'), ('UCM', 'uncommon'), ('RAR', 'rare'),)

    project = m.ForeignKey(CardProject, blank=False, null=False,)
    release = m.ForeignKey(CardRelease, blank=False, null=False,)
    type = m.ForeignKey(CardType, blank=False, null=False,)
    color = m.ForeignKey(CardColor, blank=False, null=False,)

    image = m.CharField(max_length=250, blank=True, null=True)

    attributes = m.ManyToManyField(CardAttribute, null=True, blank=True,)

    name = m.CharField(max_length=225, verbose_name=_('card name'),)
    name_slug = m.SlugField(max_length=250, unique=True, verbose_name=_('slug name'),)
    text_card = m.TextField(blank= True, null=True, verbose_name=_('card text'),)
    text_flavor = m.TextField(blank= True, null=True, verbose_name=_('card flavor text'),)
    rarity = m.CharField(max_length=3, choices=CHOICES_RARITY, default='CMN', verbose_name=_('card rarity'),)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Card'), _(u'Cards')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(Card, self).save(*args, **kwargs)



class Deck(m.Model):
    """    card deck    """

    name = m.CharField(max_length=225,  verbose_name=_('deck name'),)
    name_slug = m.SlugField(max_length=250, verbose_name=_('slug name'),)
    description = m.TextField(blank=True, null=True, verbose_name=_('description'),)
    cards = m.ManyToManyField(Card, null=True, blank=True,)

    class Meta:
        verbose_name, verbose_name_plural = _(u'Deck'), _(u'Deck')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_slug is None:
            self.name_slug = slugify(self.name)
        super(Deck, self).save(*args, **kwargs)



class Game(m.Model):
    """

    """

