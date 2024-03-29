from django.utils.translation import gettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(
    label=_(message='Metadata'), name='metadata'
)

event_document_metadata_added = namespace.add_event_type(
    label=_(message='Document metadata added'), name='document_metadata_added'
)
event_document_metadata_edited = namespace.add_event_type(
    label=_(message='Document metadata edited'), name='document_metadata_edited'
)
event_document_metadata_removed = namespace.add_event_type(
    label=_(message='Document metadata removed'), name='document_metadata_removed'
)
event_metadata_type_created = namespace.add_event_type(
    label=_(message='Metadata type created'), name='metadata_type_created'
)
event_metadata_type_edited = namespace.add_event_type(
    label=_(message='Metadata type edited'), name='metadata_type_edited'
)
event_metadata_type_relationship_updated = namespace.add_event_type(
    label=_(message='Metadata type relationship updated'),
    name='metadata_type_relationship'
)
