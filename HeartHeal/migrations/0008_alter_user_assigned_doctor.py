# Generated by Django 4.2.3 on 2023-08-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0007_rename_first_name_user_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assigned_doctor',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='HeartHeal.user'),
        ),
    ]
