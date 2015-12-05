import django


if django.VERSION < (1, 9):
    from .admin import (TaggitCounter, TaggitListFilter, TaggitStackedInline,
        TaggitTabularInline)

default_app_config = 'taggit_helpers.apps.TaggitHelpersConfig'

__version__ = '0.1.4'
