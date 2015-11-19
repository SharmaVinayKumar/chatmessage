# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageuserlist',
            name='message',
            field=models.ForeignKey(blank=True, to='chat.Message', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='messageuserlist',
            unique_together=set([('requested_user', 'to_user')]),
        ),
    ]
