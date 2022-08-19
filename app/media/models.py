from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class MediaFile(models.Model):
    url = models.CharField(max_length=200, verbose_name='URL')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.url

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
