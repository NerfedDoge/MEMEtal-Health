# Generated by Django 4.2.3 on 2023-08-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0022_post_user_alter_user_assigned_doctor_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='HeartHeal.user'),
        ),
    ]
