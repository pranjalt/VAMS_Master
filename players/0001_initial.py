# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20151201_1433'),
        ('sportsList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CwgOnboardingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('onboarding', models.ForeignKey(to='sportsList.Onboarding')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
