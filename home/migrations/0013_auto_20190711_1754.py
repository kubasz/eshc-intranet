# Generated by Django 2.1.10 on 2019-07-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_old_role_assign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wgupdate',
            name='group',
            field=models.ForeignKey(limit_choices_to=models.Q(name__endswith='WG'), on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]