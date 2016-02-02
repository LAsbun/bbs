# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tittle',
            new_name='title',
        ),
    ]
