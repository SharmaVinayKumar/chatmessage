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
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MessageUserList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(to='chat.Message')),
                ('requested_user', models.ForeignKey(related_name='requested_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
