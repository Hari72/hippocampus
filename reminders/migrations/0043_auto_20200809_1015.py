# Generated by Django 3.0.8 on 2020-08-09 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0042_auto_20200808_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 14, 10, 15, 36, 691306)),
        ),
    ]