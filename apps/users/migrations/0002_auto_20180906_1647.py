# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-06 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '菜单', 'verbose_name_plural': '菜单'},
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='url_name',
            new_name='url',
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url_type',
        ),
    ]
