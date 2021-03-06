# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-15 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170715_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costprice', models.FloatField()),
                ('sellprice', models.FloatField()),
                ('batchno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.batchdata')),
                ('itemscode_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.medicine')),
            ],
        ),
    ]
