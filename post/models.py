# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from core.models import ModelWithAuthor, ModelWithTime
from like.models import LikeAble

# Create your models here.
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)


class Post(ModelWithAuthor, ModelWithTime, LikeAble):
    title = models.CharField(max_length=50, default='')
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()
