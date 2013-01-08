# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from models import *
from django.core.urlresolvers import reverse



class IndexView(View, TemplateResponseMixin):
    """

    """
#    def get(self, request, *args, **kwargs):
#            return HttpResponse('Hello, World!')

    template_name = 'card-base.html'
    def get_context(self, request):
        context = dict()
        context['decks'] = Deck.objects.all()
        print reverse('card:deck-view')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return TemplateResponseMixin.render_to_response(self, context)


class DeckView(View, TemplateResponseMixin):
    """

    """
#    def get(self, request, *args, **kwargs):
#            return HttpResponse('Hello, World!')

    template_name = 'card-base.html'
    def get_context(self, request):
        context = dict()
        context['decks'] = Deck.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return TemplateResponseMixin.render_to_response(self, context)