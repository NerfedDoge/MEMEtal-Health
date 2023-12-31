# Generated by Django 4.2.3 on 2023-08-25 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0036_practice_image_alter_comment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 14, 15, 45, 26846, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='link_meeting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='timestamp',
            field=models.DateField(default=datetime.date(2023, 8, 25)),
        ),
    ]
