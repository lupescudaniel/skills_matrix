# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-17 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillsmatrix', '0015_auto_20170217_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='difficulty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
