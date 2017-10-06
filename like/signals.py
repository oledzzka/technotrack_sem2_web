from django.db.models.signals import post_save, post_delete

from event.models import Event, EventEnum, create_event
from like.models import Like


def post_save_like_signal(instance, created=False, *args, **kwargs):
    if created:
        create_event(instance.author, EventEnum.liked,
                      u"User {} liked {}".format(instance.author, instance.content_object), instance.content_object)
        instance.content_object.likes_count += 1
        instance.content_object.save()


def post_delete_like_signal(instance, *args, **kwargs):
    if instance.content_object:
        if instance.content_object.likes_count > 0:
            instance.content_object.likes_count -= 1
            instance.content_object.save()

post_save.connect(post_save_like_signal, Like)
post_delete.connect(post_delete_like_signal, Like)
