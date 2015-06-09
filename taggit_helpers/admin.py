from django.contrib import admin
from django.contrib.contenttypes.admin import (GenericStackedInline,
    GenericTabularInline)
from django.db.models import Count

from taggit.models import TaggedItem


class TaggitCounter():
    """
    Display (and sort by) number of Taggit tags associated with tagged items.

    Usage Example:
        from taggit_helpers import TaggitCounter


        @admin.register(MyModel)
        class MyModelAdmin(TaggitCounter, admin.ModelAdmin):
            list_display = (
                ...
                'taggit_count',
            )
    """

    def queryset(self, request):
        queryset = self.model.objects.get_query_set()
        return queryset.annotate(taggit_count=Count('tags', distinct=True))

    def taggit_count(self, obj):
        return obj.taggit_count
    taggit_count.admin_order_field = 'taggit_count'
    taggit_count.short_description = '# of Tags'


class TaggitListFilter(admin.SimpleListFilter):
    """
    Filter records by Taggit tags for the current model only.
    Tags are sorted alphabetically by name.

    Usage Example:
        from taggit_helpers import TaggitListFilter


        @admin.register(MyModel)
        class MyModelAdmin(admin.ModelAdmin):
            list_filter = [TaggitListFilter]
    """

    title = 'Tags'
    parameter_name = 'tag'

    def lookups(self, request, model_admin):
        model_tags = [tag.name for tag in
            TaggedItem.tags_for(model_admin.model)]
        model_tags.sort()
        return tuple([(tag, tag) for tag in model_tags])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(tags__name=self.value())


class TaggitInlineBase():
    """
    Base model for Taggit admin inlines.
    Use TaggitStackedInline or TaggitTabularInline.
    """
    model = TaggedItem
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'
    ordering = ('tag__name',)


class TaggitStackedInline(TaggitInlineBase, GenericStackedInline):
    """
    Add stacked inline for Taggit tags to admin.
    Tags are sorted alphabetically by name.

    Usage example:
        from taggit_helpers import TaggitStackedInline


        @admin.register(MyModel)
        class MyModelAdmin(admin.ModelAdmin):
            inlines = [TaggitStackedInline]
    """
    pass


class TaggitTabularInline(TaggitInlineBase, GenericTabularInline):
    """
    Add tabular inline for Taggit tags to admin.
    Tags are sorted alphabetically by name.

    Usage example:
        from taggit_helpers import TaggitTabularInline


        @admin.register(MyModel)
        class MyModelAdmin(admin.ModelAdmin):
            inlines = [TaggitTabularInline]
    """
    pass
