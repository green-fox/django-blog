# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_player', models.CharField(default=b'YOUTUBE', max_length=1, choices=[(b'YOUTUBE', b'youtube'), (b'DAILYMOTION', b'dailymotion'), (b'VIMEO', b'vimeo')])),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
