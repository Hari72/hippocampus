# Generated by Django 3.0.8 on 2020-07-08 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0029_auto_20200707_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 16, 55, 8, 77156)),
        ),
    ]
