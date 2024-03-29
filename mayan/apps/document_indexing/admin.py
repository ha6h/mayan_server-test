from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models.index_template_models import IndexTemplate, IndexTemplateNode


class IndexTemplateNodeInline(admin.StackedInline):
    extra = 0
    list_display = ('expression', 'enabled', 'link_documents')
    model = IndexTemplateNode


@admin.register(IndexTemplate)
class IndexTemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('document_types',)
    inlines = (IndexTemplateNodeInline,)
    list_display = ('label', 'enabled', 'get_document_types')

    def get_document_types(self, instance):
        return ', '.join(
            [
                '"{}"'.format(document_type) for document_type in instance.document_types.all()
            ]
        ) or _(message='None')

    get_document_types.short_description = _(message='Document types')
