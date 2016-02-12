# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20160202_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='app01.Admin', blank=True),
        ),
    ]
