# Generated by Django 3.0.8 on 2020-07-09 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0030_auto_20200708_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 55, 33, 916534)),
        ),
    ]
