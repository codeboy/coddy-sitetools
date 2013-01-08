# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Card, CardAttribute, CardType, CardProject, CardRelease, Deck, CardColor


class DefaultAdmin(admin.ModelAdmin):
    save_on_top = True

class MixedSlugAdmin(DefaultAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

admin.site.register(Card, MixedSlugAdmin)
admin.site.register(CardAttribute, MixedSlugAdmin)
admin.site.register(CardProject, MixedSlugAdmin)
admin.site.register(CardType, MixedSlugAdmin)
admin.site.register(CardRelease, MixedSlugAdmin)
admin.site.register(Deck, MixedSlugAdmin)
admin.site.register(CardColor, MixedSlugAdmin)

