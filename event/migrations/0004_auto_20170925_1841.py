# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-25 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20170925_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type_event',
            field=models.TextField(max_length=50),
        ),
    ]
