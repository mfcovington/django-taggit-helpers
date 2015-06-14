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

        class MyModelAdmin(TaggitCounter, admin.ModelAdmin):
            list_display = (
                ...
                'taggit_counter',
            )

    Note: Currently, the TaggableManager() field must be named 'tags'.

    Note: To avoid overcounting, set distinct=True if further annotating the queryset with Count():

        queryset.annotate(m2m_field_count=Count('m2m_field', distinct=True))
    """

    def get_queryset(self, request):
        queryset = self.model.objects.get_queryset()
        return queryset.annotate(taggit_counter=Count('tags', distinct=True))

    def taggit_counter(self, obj):
        return obj.taggit_counter
    taggit_counter.admin_order_field = 'taggit_counter'
    taggit_counter.short_description = '# of Tags'


class TaggitListFilter(admin.SimpleListFilter):
    """
    Filter records by Taggit tags for the current model only.
    Tags are sorted alphabetically by name.

    Usage Example:
        from taggit_helpers import TaggitListFilter

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

        class MyModelAdmin(admin.ModelAdmin):
            inlines = [TaggitTabularInline]
    """
    pass
