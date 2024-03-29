from django.utils.translation import gettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(
    label=_(message='Signature captures'),
    name='signature_captures'
)

event_signature_capture_created = namespace.add_event_type(
    label=_(message='Signature capture created'),
    name='signature_capture_created'
)
event_signature_capture_deleted = namespace.add_event_type(
    label=_(message='Signature capture deleted'),
    name='signature_capture_deleted'
)
event_signature_capture_edited = namespace.add_event_type(
    label=_(message='Signature capture edited'),
    name='signature_capture_edited'
)
