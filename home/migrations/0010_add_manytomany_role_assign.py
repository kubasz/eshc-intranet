# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_auto_20190617_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='assigned_to_many',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role',
            name='ldap_groups',
            field=models.ManyToManyField(blank=True, to='home.LdapGroup'),
        ),
    ]
