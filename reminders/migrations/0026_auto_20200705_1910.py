# Generated by Django 3.0.8 on 2020-07-05 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0025_auto_20200705_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='byWho',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='forWho',
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remind_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 19, 10, 21, 39214)),
        ),
    ]