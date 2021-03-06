# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-23 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillsmatrix', '0010_auto_20170121_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracredit',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='extracredit',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='extracredit',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='extra_credit_tokens',
        ),
        migrations.AlterField(
            model_name='developer',
            name='start_date',
            field=models.DateField(default=datetime.date(2017, 1, 23)),
        ),
        migrations.DeleteModel(
            name='ExtraCredit',
        ),
    ]
