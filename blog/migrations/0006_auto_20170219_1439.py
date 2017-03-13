# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, null=True, verbose_name='image', max_length=255),
        ),
    ]