# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0004_auto_20151207_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManagement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_quantity', models.IntegerField(null=True, blank=True)),
                ('quantity_left', models.IntegerField(null=True, blank=True)),
                ('issue_date', models.DateTimeField(null=True, blank=True)),
                ('return_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(blank=True, to='sportsList.Asset', null=True)),
                ('school', models.ForeignKey(blank=True, to='sportsList.School', null=True)),
                ('sports', models.ForeignKey(blank=True, to='sportsList.Sports', null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_quantity', models.IntegerField(null=True, blank=True)),
                ('quantity_left', models.IntegerField(null=True, blank=True)),
                ('asset', models.ForeignKey(blank=True, to='sportsList.Asset', null=True)),
                ('vendor', models.ForeignKey(blank=True, to='sportsList.Vendor', null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vendor',
            name='assets',
            field=models.ManyToManyField(to='sportsList.Asset', through='sportsList.VendorAsset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vendor',
            name='sports',
            field=models.ManyToManyField(to='sportsList.Sports'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assetmanagement',
            name='vendor',
            field=models.ForeignKey(blank=True, to='sportsList.Vendor', null=True),
            preserve_default=True,
        ),
    ]
