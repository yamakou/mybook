# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='書籍名')),
                ('publisher', models.CharField(max_length=255, verbose_name='出版社', blank=True)),
                ('page', models.IntegerField(verbose_name='ページ数', default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('comment', models.TextField(verbose_name='コメント', blank=True)),
                ('book', models.ForeignKey(related_name='impressions', verbose_name='書籍', to='cms.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
