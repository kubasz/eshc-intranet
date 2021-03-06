# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-23 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date_conv', models.DateField(verbose_name='date convened')),
            ],
        ),
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_file', models.FileField(upload_to='minutes/')),
                ('gm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.GM')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.GM')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WgUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.GM')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]
