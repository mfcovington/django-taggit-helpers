*********************
django-taggit-helpers
*********************

``django-taggit-helpers`` makes it easier to work with admin pages of models associated with ``django-taggit`` tags.
Information about ``django-taggit`` is available on `GitHub <https://github.com/alex/django-taggit>`_ and `Read the Docs <http://django-taggit.readthedocs.org/en/latest/index.html>`_.

.. contents:: :local:

Installation
============

**PyPI**

.. code-block:: sh

    pip install django-taggit-helpers

**GitHub**

.. code-block:: sh

    pip install https://github.com/mfcovington/django-taggit-helpers/releases/download/0.0.0/django-taggit-helpers-0.0.0.tar.gz

Helper Classes
==============

``TaggitCounter``
-----------------

Display (and sort by) number of Taggit tags associated with tagged items.

.. code-block:: python

    from taggit_helpers import TaggitCounter

    class MyModelAdmin(TaggitCounter, admin.ModelAdmin):    # TaggitCounter before ModelAdmin
        list_display = (
            ...
            'taggit_count',
        )

*Note:* Currently, the ``TaggableManager()`` field must be named ``tags``.

*Note:* To avoid overcounting, set ``distinct=True`` if further annotating the queryset with ``Count()``:

.. code-block:: python

    queryset.annotate(m2m_field_count=Count('m2m_field', distinct=True))

``TaggitListFilter``
--------------------

Filter records by Taggit tags for the current model only.
Tags are sorted alphabetically by name.

.. code-block:: python

    from taggit_helpers import TaggitListFilter

    class MyModelAdmin(admin.ModelAdmin):
        list_filter = [TaggitListFilter]

``TaggitStackedInline``
-----------------------

Add stacked inline for Taggit tags to admin.
Tags are sorted alphabetically by name.

.. code-block:: python

    from taggit_helpers import TaggitStackedInline

    class MyModelAdmin(admin.ModelAdmin):
        inlines = [TaggitStackedInline]

``TaggitTabularInline``
-----------------------

Add tabular inline for Taggit tags to admin.
Tags are sorted alphabetically by name.

.. code-block:: python

    from taggit_helpers import TaggitTabularInline

    class MyModelAdmin(admin.ModelAdmin):
        inlines = [TaggitTabularInline]

*Version 0.0.0*
