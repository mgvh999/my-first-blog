# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170306_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
