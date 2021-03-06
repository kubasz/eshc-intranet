# Generated by Django 2.1.10 on 2019-11-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('finance', '0001_initial'), ('finance', '0002_auto_20191105_1436'), ('finance', '0003_financeconfig_monthlyrent')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qboRealmId', models.BigIntegerField(blank=True, null=True, verbose_name='(API) QBO Realm ID')),
                ('qboAccessToken', models.CharField(blank=True, max_length=256, null=True, verbose_name='(API) QBO Access Toekn')),
                ('qboAccessTimeout', models.DateTimeField(blank=True, null=True, verbose_name='(API) QBO Access Expiry')),
                ('qboRefreshToken', models.CharField(blank=True, max_length=256, null=True, verbose_name='(API) QBO Refresh Token')),
                ('qboRefreshTimeout', models.DateTimeField(blank=True, null=True, verbose_name='(API) QBO Refresh Expiry')),
                ('monthlyRent', models.DecimalField(decimal_places=2, default=300.0, max_digits=8, verbose_name='Monthly rent')),
            ],
        ),
    ]
