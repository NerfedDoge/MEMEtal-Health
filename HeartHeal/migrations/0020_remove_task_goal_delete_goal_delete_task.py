# Generated by Django 4.2.3 on 2023-08-17 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0019_goal_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='goal',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
