# Generated by Django 3.0.8 on 2020-07-07 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0028_auto_20200705_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 7, 35, 42, 216783)),
        ),
    ]
