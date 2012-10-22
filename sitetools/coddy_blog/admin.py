# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Post


class PostAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(Post, PostAdmin)
