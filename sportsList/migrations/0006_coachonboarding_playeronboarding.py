# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0005_auto_20151207_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachOnboarding',
            fields=[
                ('coach_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('email_id', models.CharField(max_length=100, blank=True)),
                ('contact_no', models.BigIntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('total_yrs_exp', models.IntegerField(null=True, blank=True)),
                ('sec_ans1', models.CharField(max_length=100, blank=True)),
                ('sec_ans2', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'coach_onboarding',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerOnboarding',
            fields=[
                ('player_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('email_id', models.CharField(max_length=100, blank=True)),
                ('contact_no', models.BigIntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('total_yrs_exp', models.IntegerField(null=True, blank=True)),
                ('sec_ans1', models.CharField(max_length=100, blank=True)),
                ('sec_ans2', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'player_onboarding',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
