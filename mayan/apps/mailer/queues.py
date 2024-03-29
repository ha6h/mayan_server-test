from django.utils.translation import gettext_lazy as _

from mayan.apps.task_manager.classes import CeleryQueue
from mayan.apps.task_manager.workers import worker_c

queue_mailing = CeleryQueue(
    label=_(message='Mailing'), name='mailing', worker=worker_c
)

queue_mailing.add_task_type(
    dotted_path='mayan.apps.mailer.tasks.task_send_object',
    label=_(message='Send object')
)
