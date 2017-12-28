from django.conf import settings
from templated_email import get_templated_mail


def send_fake_email(template, context, from_mail, recipient_list):
    if settings.DEBUG:
        recipient_list = [admin[0] for admin in settings.ADMINS]

    email = get_templated_mail(
        template,
        context,
        from_mail,
        recipient_list,
    )
    email.send()
