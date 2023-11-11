from django.utils.translation import gettext_lazy as _

from .classes import Dashboard

dashboard_administrator = Dashboard(
    name='administrator', label=_(message='Administrator dashboard')
)
