# Generated by Django 3.0.8 on 2020-08-04 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0034_auto_20200802_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 6, 43, 0, 752616)),
        ),
    ]
