# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from core.models import ModelWithAuthor, ModelWithTime

# Create your models here.
from like.models import LikeAble


class Comment(ModelWithAuthor, ModelWithTime, LikeAble):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey()
    text = models.TextField()

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __unicode__(self):
        return str(self.content_object) + ' : ' + self.author.username

    def __str__(self):
        return self.__unicode__()


class CommentAble(models.Model):
    comments = fields.GenericRelation(Comment)
    comments_count = models.PositiveIntegerField()

    class Meta:
        abstract = True
