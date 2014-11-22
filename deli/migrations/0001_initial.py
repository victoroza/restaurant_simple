# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('sunday', models.BooleanField()),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(related_name='foodItem', to='deli.Restaurant'),
            preserve_default=True,
        ),
    ]
