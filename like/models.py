# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from core.models import ModelWithAuthor, ModelWithTime

# Create your models here.


class Like(ModelWithAuthor, ModelWithTime):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey()

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __unicode__(self):
        return str(self.author) + ' : ' + str(self.content_object)


class LikeAble(models.Model):
    likes = fields.GenericRelation(Like)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
