# Generated by Django 4.2.3 on 2023-08-05 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0012_meeting_available_meeting_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='available',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time',
        ),
        migrations.AddField(
            model_name='meeting',
            name='link_meeting',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='duration',
            field=models.DurationField(default=datetime.time(1, 0)),
        ),
    ]
