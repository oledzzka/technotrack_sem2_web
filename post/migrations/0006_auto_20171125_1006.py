# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-25 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20171005_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.user_directory_path),
        ),
    ]