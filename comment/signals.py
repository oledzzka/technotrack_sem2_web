from django.db.models.signals import post_save, post_delete

from comment.models import Comment


def create_comment(instance, created=False, *args, **kwargs):
    if created:
        instance.content_object.comments_count += 1
        instance.comments.save()


def delete_comment(instance, *args, **kwargs):
    if instance.content_object:
        instance.content_object.comments_count -= 1


post_save.connect(create_comment, Comment)
post_delete.connect(delete_comment, Comment)
