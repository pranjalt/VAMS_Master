# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0005_auto_20151207_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'asset',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assetmanagement',
            fields=[
                ('asset_mgmt_id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset_quantity', models.IntegerField(null=True, blank=True)),
                ('issue_date', models.DateTimeField(null=True, blank=True)),
                ('return_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(blank=True, to='assetManagement.Asset', null=True)),
            ],
            options={
                'db_table': 'assetmanagement',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.IntegerField(serialize=False, primary_key=True)),
                ('school_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'school',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'vendor',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorSports',
            fields=[
                ('vendorsport_id', models.IntegerField(serialize=False, primary_key=True)),
                ('sports', models.ForeignKey(related_name='sport1', to='sportsList.Sports')),
                ('vendor', models.ForeignKey(to='assetManagement.Vendor')),
            ],
            options={
                'db_table': 'vendor_sports',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorsportsAsset',
            fields=[
                ('vendorsport_asset_id', models.IntegerField(serialize=False, primary_key=True)),
                ('max_quantity', models.IntegerField(null=True, blank=True)),
                ('quantity_left', models.IntegerField(null=True, blank=True)),
                ('asset', models.ForeignKey(blank=True, to='assetManagement.Asset', null=True)),
                ('vendor_sport', models.ForeignKey(blank=True, to='assetManagement.VendorSports', null=True)),
            ],
            options={
                'db_table': 'vendorsports_asset',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assetmanagement',
            name='school',
            field=models.ForeignKey(blank=True, to='assetManagement.School', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assetmanagement',
            name='sports',
            field=models.ForeignKey(related_name='sport2', blank=True, to='sportsList.Sports', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assetmanagement',
            name='vendor',
            field=models.ForeignKey(blank=True, to='assetManagement.Vendor', null=True),
            preserve_default=True,
        ),
    ]
