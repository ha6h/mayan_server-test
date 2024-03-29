from django.utils.translation import gettext_lazy as _

from mayan.apps.rest_api import serializers

from .models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'url': {
                'label': _(message='URL'),
                'lookup_url_kwarg': 'key_id',
                'view_name': 'rest_api:key-detail'
            }
        }
        fields = (
            'algorithm', 'creation_date', 'expiration_date', 'fingerprint',
            'id', 'key_data', 'key_type', 'length', 'url', 'user_id'
        )
        model = Key
        read_only_fields = (
            'algorithm', 'creation_date', 'expiration_date', 'fingerprint',
            'id', 'key_type', 'length', 'url', 'user_id'
        )
