# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_auto_20161020_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='is_public',
            field=models.BooleanField(default=False,
                                      verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f\u0435\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0443'),
        ),
    ]
