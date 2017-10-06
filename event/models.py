# coding=utf-8
from __future__ import unicode_literals

from django.contrib.contenttypes import fields
from django.db import models

# Create your models here.
from django.contrib.contenttypes.models import ContentType

from core.models import ModelWithAuthor, ModelWithTime


class EventEnum(enumerate):
    create_post = u"create_post"
    delete_post = u"delete_post"
    liked = u"liked"
    commented = u"commented"
    subscribed = u"subscribed"
    unsubscribed = u"unsubscribed"


class Event(ModelWithAuthor, ModelWithTime):

    type_event = models.CharField(max_length=50)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object_event = fields.GenericForeignKey()

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.__unicode__()


def create_event(author, type_event, text, object_event):
    event = Event()
    event.author = author
    event.type_event = type_event
    event.text = text
    event.object_event = object_event
    event.save()
