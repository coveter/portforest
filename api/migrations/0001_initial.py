# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=128, verbose_name=b'\xe3\x82\xbf\xe3\x82\xb9\xe3\x82\xaf')),
                ('complete', models.BooleanField(default=False, verbose_name=b'\xe7\x8a\xb6\xe6\x85\x8b')),
                ('comment', models.CharField(max_length=512, verbose_name=b'\xe3\x82\xb3\xe3\x83\xa1\xe3\x83\xb3\xe3\x83\x88', blank=True)),
                ('done_date', models.DateField(null=True, verbose_name=b'\xe5\xae\x8c\xe4\xba\x86\xe6\x97\xa5', blank=True)),
                ('user', models.ForeignKey(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
