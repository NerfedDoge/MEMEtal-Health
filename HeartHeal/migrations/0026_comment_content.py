# Generated by Django 4.2.3 on 2023-08-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0025_post_timestamp_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
