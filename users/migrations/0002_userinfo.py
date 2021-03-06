# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('addressLocality', models.CharField(max_length=255, null=True, blank=True)),
                ('addressSubLocality', models.CharField(max_length=100, null=True, blank=True)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('addressLogitude', models.FloatField(null=True, blank=True)),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('flag', models.BooleanField(default=0)),
                ('owner', models.ForeignKey(related_name='UserInfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
