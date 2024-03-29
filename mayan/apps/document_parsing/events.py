from django.utils.translation import gettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(
    label=_(message='Document parsing'), name='document_parsing'
)

event_parsing_document_file_content_deleted = namespace.add_event_type(
    label=_(message='Document file parsed content deleted'),
    name='document_content_deleted'
)
event_parsing_document_file_submitted = namespace.add_event_type(
    label=_(message='Document file submitted for parsing'), name='version_submit'
)
event_parsing_document_file_finished = namespace.add_event_type(
    label=_(message='Document file parsing finished'), name='version_finish'
)
