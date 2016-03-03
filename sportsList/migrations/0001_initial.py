# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyOnboarding',
            fields=[
                ('acd_reg_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('estd', models.DateField(null=True, blank=True)),
                ('website', models.CharField(max_length=50, null=True, blank=True)),
                ('contact_no', models.BigIntegerField(null=True, blank=True)),
                ('email_id', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'academy_onboarding',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AcademySports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acd_reg_id', models.ForeignKey(to='sportsList.AcademyOnboarding')),
            ],
            options={
                'db_table': 'academy_sports',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(serialize=False, primary_key=True)),
                ('street1', models.CharField(max_length=30, null=True, blank=True)),
                ('street2', models.CharField(max_length=30, null=True, blank=True)),
                ('zipcode', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(serialize=False, primary_key=True)),
                ('city_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(serialize=False, primary_key=True)),
                ('country_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'country',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.AutoField(serialize=False, primary_key=True)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'gender',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.AutoField(serialize=False, primary_key=True)),
                ('level', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'level',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Onboarding',
            fields=[
                ('reg_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('email_id', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_no', models.BigIntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('total_yrs_exp', models.IntegerField(null=True, blank=True)),
                ('sec_ans1', models.CharField(max_length=100, null=True, blank=True)),
                ('sec_ans2', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.ForeignKey(db_column=b'address', blank=True, to='sportsList.Address', null=True)),
                ('gender', models.ForeignKey(db_column=b'gender', blank=True, to='sportsList.Gender', null=True)),
            ],
            options={
                'db_table': 'onboarding',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_id', models.IntegerField(serialize=False, primary_key=True)),
                ('province_name', models.CharField(max_length=20, null=True, blank=True)),
                ('country', models.ForeignKey(blank=True, to='sportsList.Country', null=True)),
            ],
            options={
                'db_table': 'province',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(serialize=False, primary_key=True)),
                ('role', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'role',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecurityQuestions',
            fields=[
                ('sec_ques_id', models.AutoField(serialize=False, primary_key=True)),
                ('sec_ques', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'security_questions',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('sports_id', models.IntegerField(serialize=False, primary_key=True)),
                ('sports_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'sports',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('yrs_of_exp', models.IntegerField(null=True, blank=True)),
                ('period_from', models.DateField(null=True, blank=True)),
                ('period_to', models.DateField(null=True, blank=True)),
                ('place', models.CharField(max_length=30, null=True, blank=True)),
                ('achievements', models.CharField(max_length=500, null=True, blank=True)),
                ('level', models.ForeignKey(db_column=b'level', blank=True, to='sportsList.Level', null=True)),
                ('reg_id', models.ForeignKey(to='sportsList.Onboarding')),
            ],
            options={
                'db_table': 'team',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('reg_id', 'name')]),
        ),
        migrations.AddField(
            model_name='onboarding',
            name='role',
            field=models.ForeignKey(db_column=b'role', blank=True, to='sportsList.Role', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onboarding',
            name='sec_ques',
            field=models.ForeignKey(db_column=b'sec_ques2', blank=True, to='sportsList.SecurityQuestions', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onboarding',
            name='sports',
            field=models.ForeignKey(db_column=b'sports', blank=True, to='sportsList.Sports', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(db_column=b'country', blank=True, to='sportsList.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(db_column=b'city', blank=True, to='sportsList.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(db_column=b'country', blank=True, to='sportsList.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(db_column=b'province', blank=True, to='sportsList.Province', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='academysports',
            name='sports_id',
            field=models.ForeignKey(to='sportsList.Sports'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='academysports',
            unique_together=set([('acd_reg_id', 'sports_id')]),
        ),
        migrations.AddField(
            model_name='academyonboarding',
            name='address',
            field=models.ForeignKey(db_column=b'address', blank=True, to='sportsList.Address', null=True),
            preserve_default=True,
        ),
    ]
