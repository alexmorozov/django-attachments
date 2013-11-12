# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import attachments.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=1024, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('attachment_file', models.FileField(upload_to=attachments.models.attachment_upload, max_length=1024, verbose_name='\u0444\u0430\u0439\u043b')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('creator', models.ForeignKey(related_name='created_attachments', verbose_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0444\u0430\u0439\u043b',
                'verbose_name_plural': '\u0444\u0430\u0439\u043b\u044b',
                'permissions': (('delete_foreign_attachments', 'Can delete foreign attachments'),),
            },
        ),
    ]
