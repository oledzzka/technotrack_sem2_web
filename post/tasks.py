# coding=utf-8
from __future__ import absolute_import, unicode_literals

from celery.decorators import periodic_task
from celery.task.schedules import crontab
from datetime import timedelta
from django.utils import timezone

from templated_email import InlineImage

from core.helpers import send_fake_email
from celery import task
from post.models import Post
from core.models import User


@task(bind=True)
def send_email(self, template, context, from_mail, recipient_list):
    try:
        post_id = context.get('post_id')
        if post_id:
            posts = Post.objects.all().filter(id=post_id)
            if posts:
                post = posts[0]
                context['image'] = InlineImage('photo.jpeg', open(post.photo.path, 'rb').read(), 'jpeg')
        send_fake_email(template, context, from_mail, recipient_list)
    except Exception as exc:
        self.retry(exc=exc, countdown=5, max_retries=3)


@periodic_task(run_every=crontab(minute=1), bind=True)
def every_monday_morning(self):
    print "start"
    qs = User.objects.all().filter(last_login__lt=timezone.now() - timedelta(1))
    context = {
        'subject': "Давно не заходил",
        'title': "Давно не заходил",
        'text': "Давно не заходил",
        'plain': "Давно не заходил"
    }
    try:
        send_fake_email('base', context, 'no@mail.ru', qs.values_list("email", flat=True))
    except Exception as exc:
        self.retry(exc=exc, countdown=5, max_retries=3)
