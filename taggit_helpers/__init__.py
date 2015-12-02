import django


if django.VERSION < (1, 9):
    from .admin import (TaggitCounter, TaggitListFilter, TaggitStackedInline,
        TaggitTabularInline)

__version__ = '0.1.3'
