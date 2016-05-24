# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20160524_0707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organizer',
            new_name='Organizers',
        ),
        migrations.RenameModel(
            old_name='Venue',
            new_name='Venues',
        ),
    ]
