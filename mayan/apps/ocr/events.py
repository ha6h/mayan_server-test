from django.utils.translation import gettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(
    label=_(message='OCR'), name='ocr'
)

event_ocr_document_version_content_deleted = namespace.add_event_type(
    label=_(message='Document version OCR content deleted'),
    name='document_content_deleted'
)
event_ocr_document_version_page_content_edited = namespace.add_event_type(
    label=_(message='Document version page OCR content edited'),
    name='document_version_page_content_edited'
)
event_ocr_document_version_submitted = namespace.add_event_type(
    label=_(message='Document version submitted for OCR'),
    name='document_version_submit'
)
event_ocr_document_version_finished = namespace.add_event_type(
    label=_(message='Document version OCR finished'),
    name='document_version_finish'
)
