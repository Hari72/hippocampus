# Generated by Django 3.0.3 on 2020-02-23 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_reminder_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remind_me_at',
            field=models.DateTimeField(default=datetime.date(2020, 2, 28)),
        ),
    ]