# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=20)),
                ('item_price', models.FloatField(max_length=20)),
                ('item_image', models.ImageField(null=True, upload_to=items.models.upload_to, blank=True)),
                ('item_description', models.CharField(default=b'Basic Needs', max_length=100)),
                ('item_quantity', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
