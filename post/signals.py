# coding=utf-8
import os
from django.db.models.signals import post_save, post_delete

from event.models import Event, EventEnum, create_event
from post.models import Post


def post_save_signal(instance, created=False, *args, **kwargs):
    if created:
        create_event(instance.author, EventEnum.create_post,
                  u"User {} create post {}".format(instance.author, instance.title), instance)


def post_delete_signal(instance, *args, **kwargs):
    create_event(instance.author, EventEnum.delete_post,
                  u"User {} delete post {}".format(instance.author, instance.title), instance)

post_save.connect(post_save_signal, Post)
post_delete.connect(post_delete_signal, Post)
