from django import forms
from django.forms.formsets import formset_factory
from django.utils.translation import gettext_lazy as _

from .models import EventSubscription, ObjectEventSubscription


class EventTypeUserRelationshipForm(forms.Form):
    namespace = forms.CharField(
        label=_(message='Namespace'), required=False,
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
        )
    )
    label = forms.CharField(
        label=_(message='Label'), required=False,
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
        )
    )
    subscription = forms.ChoiceField(
        label=_(message='Subscription'),
        widget=forms.RadioSelect(), choices=(
            ('none', _(message='No')),
            ('subscribed', _(message='Subscribed'))
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs
        )

        if 'stored_event_type' in self.initial:
            self.fields['namespace'].initial = self.initial['stored_event_type'].namespace
            self.fields['label'].initial = self.initial['stored_event_type'].label

            subscription = EventSubscription.objects.get_for(
                stored_event_type=self.initial['stored_event_type'],
                user=self.initial['user'],
            )

            if subscription.exists():
                self.fields['subscription'].initial = 'subscribed'
            else:
                self.fields['subscription'].initial = 'none'

    def save(self):
        subscription = EventSubscription.objects.get_for(
            stored_event_type=self.initial['stored_event_type'],
            user=self.initial['user'],
        )

        if self.cleaned_data['subscription'] == 'none':
            subscription.delete()
        elif self.cleaned_data['subscription'] == 'subscribed':
            if not subscription.exists():
                EventSubscription.objects.create_for(
                    stored_event_type=self.initial['stored_event_type'],
                    user=self.initial['user']
                )


EventTypeUserRelationshipFormSet = formset_factory(
    form=EventTypeUserRelationshipForm, extra=0
)


class ObjectEventTypeUserRelationshipForm(forms.Form):
    namespace = forms.CharField(
        label=_(message='Namespace'), required=False,
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
        )
    )
    label = forms.CharField(
        label=_(message='Label'), required=False,
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
        )
    )
    subscription = forms.ChoiceField(
        label=_(message='Subscription'),
        widget=forms.RadioSelect(), choices=(
            ('none', _(message='No')),
            ('subscribed', _(message='Subscribed'))
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs
        )

        self.fields['namespace'].initial = self.initial['stored_event_type'].namespace
        self.fields['label'].initial = self.initial['stored_event_type'].label

        subscription = ObjectEventSubscription.objects.get_for(
            obj=self.initial['object'],
            stored_event_type=self.initial['stored_event_type'],
            user=self.initial['user'],
        )

        if subscription.exists():
            self.fields['subscription'].initial = 'subscribed'
        else:
            self.fields['subscription'].initial = 'none'

    def save(self):
        subscription = ObjectEventSubscription.objects.get_for(
            obj=self.initial['object'],
            stored_event_type=self.initial['stored_event_type'],
            user=self.initial['user'],
        )

        if self.cleaned_data['subscription'] == 'none':
            subscription.delete()
        elif self.cleaned_data['subscription'] == 'subscribed':
            if not subscription.exists():
                ObjectEventSubscription.objects.create_for(
                    obj=self.initial['object'],
                    stored_event_type=self.initial['stored_event_type'],
                    user=self.initial['user']
                )


ObjectEventTypeUserRelationshipFormSet = formset_factory(
    form=ObjectEventTypeUserRelationshipForm, extra=0
)
