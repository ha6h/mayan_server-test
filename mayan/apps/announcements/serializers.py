from django.utils.translation import gettext_lazy as _

from mayan.apps.rest_api import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        extra_kwargs = {
            'url': {
                'label': _(message='URL'),
                'lookup_url_kwarg': 'announcement_id',
                'view_name': 'rest_api:announcement-detail'
            }
        }
        fields = (
            'end_datetime', 'enabled', 'label', 'id', 'start_datetime',
            'text', 'url'
        )
        model = Announcement
