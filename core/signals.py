from django.db.models.signals import post_save, m2m_changed, post_delete

from event.models import EventEnum, create_event
from models import ModelWithAuthor, User
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def model_with_author_save(instance, created=False, *args, **kwargs):
    if created:
        instance.author.objects_count += 1
        instance.author.save()


def model_with_author_post_delete(instance, *args, **kwargs):

    if instance.author.objects_count > 0:
        instance.author.objects_count -= 1
        instance.author.save()


def user_subscription(incstance, *args, **kwargs):
    if kwargs['action'] == "post_add":
        for pk in kwargs['pk_set']:
            create_event(incstance, EventEnum.subscribed,
                          "User {} subscribed on {} ".format(incstance, User.objects.get(pk=pk)),
                          User.objects.get(pk=pk))
    elif kwargs['action'] == "post_remove":
        for pk in kwargs['pk_set']:
            create_event(incstance, EventEnum.unsubscribed,
                          "User {} remove from {} news".format(incstance, User.objects.get(pk=pk)),
                          User.objects.get(pk=pk))


def user_update(instance, created=False, *args, **kwargs):
    if not created:
        create_event(instance, EventEnum.unsubscribed,
                     "User {} update your profile".format(instance), instance)


for model in ModelWithAuthor.__subclasses__():
    post_save.connect(model_with_author_save, model)
    post_delete.connect(model_with_author_post_delete, model)

m2m_changed.connect(user_subscription, User)
# post_save.connect(user_update, User)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
