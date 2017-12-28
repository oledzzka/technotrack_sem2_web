# coding=utf-8
import os

from django.db.models.signals import post_save, post_delete

from event.models import EventEnum, create_event
from instagram import settings
from post.models import Post
from post.tasks import send_email


def post_save_signal(instance, created=False, *args, **kwargs):
    if created:
        create_event(instance.author, EventEnum.create_post,
                  u"User {} create post {}".format(instance.author, instance.title), instance)
    for user in instance.author.sub_users.all():
        context = {
            'subject': "{} create post".format(instance.author.username),
            'title': "{} создал пост".format(instance.author.username.encode(encoding='utf-8')),
            'post_id': instance.id,
            'text': "{}".format(instance.title.encode(encoding='utf-8')),
            'plain': "{} создал пост {}".format(instance.author.username.encode(encoding='utf-8'),
                                                instance.title.encode(encoding='utf-8'))
        }
        send_email.apply_async(['post/post_created', context, "noreply@mail.ru", [user.email]])


def post_delete_signal(instance, *args, **kwargs):
    create_event(instance.author, EventEnum.delete_post,
                  u"User {} delete post {}".format(instance.author, instance.title), instance)

post_save.connect(post_save_signal, Post)
post_delete.connect(post_delete_signal, Post)
