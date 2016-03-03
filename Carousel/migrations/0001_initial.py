# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0006_coachonboarding_playeronboarding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel_video_video',
            fields=[
                ('video_id', models.AutoField(serialize=False, primary_key=True)),
                ('movie', models.FileField(upload_to=b'', blank=True)),
                ('movie_url', models.CharField(max_length=255, blank=True)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('auto_play', models.BooleanField(default=False)),
                ('auto_hide', models.BooleanField(default=False)),
                ('fullscreen', models.BooleanField(default=True)),
                ('loop', models.BooleanField(default=False)),
                ('bgcolor', models.CharField(default=b'000000', max_length=6)),
                ('textcolor', models.CharField(default=b'FFFFFF', max_length=6)),
                ('seekbarcolor', models.CharField(default=b'13ABEC', max_length=6)),
                ('seekbarbgcolor', models.CharField(default=b'333333', max_length=6)),
                ('loadingbarcolor', models.CharField(default=b'828282', max_length=6)),
                ('buttonoutcolor', models.CharField(default=b'333333', max_length=6)),
                ('buttonovercolor', models.CharField(default=b'000000', max_length=6)),
                ('buttonhighlightcolor', models.CharField(default=b'FFFFFF', max_length=6)),
                ('sports', models.ForeignKey(blank=True, to='sportsList.Sports', null=True)),
            ],
            options={
                'db_table': 'Carousel_video_video',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SportsSubtype',
            fields=[
                ('subtype_id', models.AutoField(serialize=False, primary_key=True)),
                ('sports_subtype', models.CharField(max_length=30, null=True, blank=True)),
                ('sports', models.ForeignKey(blank=True, to='sportsList.Sports', null=True)),
            ],
            options={
                'db_table': 'Carousel_subtype',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='carousel_video_video',
            name='subtype',
            field=models.ForeignKey(blank=True, to='Carousel.SportsSubtype', null=True),
            preserve_default=True,
        ),
    ]
