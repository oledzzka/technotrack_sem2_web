import os
from django.db.models.signals import pre_save

from image.models import ModelWithImage


def pre_save_signal(instance, created = True, *args, **kwargs):
    dir_name = instance.image.upload_to
    if not os.path.isdir(dir_name):
        try:
            os.remove(dir_name)
        except:
            pass
        os.mkdir(dir_name)


for model in ModelWithImage.__subclasses__():
    pre_save.connect(pre_save_signal, model)
