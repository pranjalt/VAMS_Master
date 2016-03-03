# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default='', help_text='Please supply the product code.', max_length=16, verbose_name='code')),
                ('price', models.DecimalField(default=0.0, help_text='Please supply the current retail price of this product.', verbose_name='price', max_digits=10, decimal_places=2)),
                ('description', cms.models.fields.PlaceholderField(slotname='product_description', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(default='', help_text='Please supply the product name.', max_length=128, verbose_name='name')),
                ('slug', models.SlugField(default='', help_text='Please supply the product slug.', max_length=128, verbose_name='slug')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='products.Product', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'products_product_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'product Translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
