# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190617_1841'),
        ('users', '0006_profile_preferred_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='extra_ldap_groups',
            field=models.ManyToManyField(to='home.LdapGroup'),
        ),
    ]
