# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d', blank=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
