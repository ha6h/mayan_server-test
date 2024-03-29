import logging

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from mayan.apps.databases.model_mixins import ExtraDataModelMixin

from ..managers import (
    FavoriteDocumentManager, ValidFavoriteDocumentProxyManager,
    ValidFavoriteDocumentManager
)

from .document_models import Document

__all__ = ('FavoriteDocument',)
logger = logging.getLogger(name=__name__)


class FavoriteDocument(ExtraDataModelMixin, models.Model):
    """
    Keeps a list of the favorited documents of a given user.
    """
    user = models.ForeignKey(
        db_index=True, editable=False, on_delete=models.CASCADE,
        to=settings.AUTH_USER_MODEL, verbose_name=_(message='User')
    )
    document = models.ForeignKey(
        editable=False, on_delete=models.CASCADE, related_name='favorites',
        to=Document, verbose_name=_(message='Document')
    )
    datetime_added = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name=_(message='Date and time added')
    )

    objects = FavoriteDocumentManager()
    valid = ValidFavoriteDocumentManager()

    class Meta:
        ordering = ('datetime_added',)
        verbose_name = _(message='Favorite document')
        verbose_name_plural = _(message='Favorite documents')

    def __str__(self):
        return str(self.document)

    def natural_key(self):
        return (
            self.document.natural_key(), self.user.natural_key()
        )
    natural_key.dependencies = [
        'documents.Document', settings.AUTH_USER_MODEL
    ]


class FavoriteDocumentProxy(Document):
    objects = models.Manager()
    valid = ValidFavoriteDocumentProxyManager()

    class Meta:
        proxy = True
