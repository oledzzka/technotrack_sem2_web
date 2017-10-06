from __future__ import unicode_literals

import os
from django.db import models

# Create your models here.
from core.models import ModelWithAuthor, ModelWithTime
from instagram.settings import MEDIA_ROOT


class ModelWithImage(ModelWithAuthor, ModelWithTime):
    image = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'image'))

    class Meta:
        abstract = True

