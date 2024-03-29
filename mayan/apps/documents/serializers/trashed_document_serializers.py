from django.utils.translation import gettext_lazy as _

from mayan.apps.rest_api import serializers

from ..models.trashed_document_models import TrashedDocument

from .document_serializers import DocumentSerializer


class TrashedDocumentSerializer(DocumentSerializer):
    image_url = serializers.HyperlinkedIdentityField(
        label=_(message='Image URL'), lookup_url_kwarg='document_id',
        view_name='rest_api:trasheddocument-image'
    )
    restore_url = serializers.HyperlinkedIdentityField(
        label=_(message='Restore URL'), lookup_url_kwarg='document_id',
        view_name='rest_api:trasheddocument-restore'
    )

    class Meta:
        extra_kwargs = {
            'url': {
                'label': _(message='URL'),
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:trasheddocument-detail'
            }
        }
        fields = sorted(
            DocumentSerializer.Meta.fields + (
                'image_url', 'restore_url', 'trashed_date_time'
            )
        )
        model = TrashedDocument
        read_only_fields = sorted(
            DocumentSerializer.Meta.read_only_fields + (
                'image_url', 'restore_url', 'trashed_date_time'
            )
        )
