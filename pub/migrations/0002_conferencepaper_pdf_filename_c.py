# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencepaper',
            name='pdf_filename_c',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]
