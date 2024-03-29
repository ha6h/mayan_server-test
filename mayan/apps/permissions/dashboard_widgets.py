from django.apps import apps
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from mayan.apps.dashboards.classes import DashboardWidgetNumeric

from .icons import icon_role_list
from .permissions import permission_role_view


class DashboardWidgetRoleTotal(DashboardWidgetNumeric):
    icon = icon_role_list
    label = _(message='Total roles')
    link = reverse_lazy(viewname='permissions:role_list')

    def get_count(self):
        AccessControlList = apps.get_model(
            app_label='acls', model_name='AccessControlList'
        )
        Role = apps.get_model(
            app_label='permissions', model_name='Role'
        )

        return AccessControlList.objects.restrict_queryset(
            permission=permission_role_view, user=self.request.user,
            queryset=Role.objects.all()
        ).count()
