# Generated by Django 3.0.8 on 2020-07-27 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0032_auto_20200709_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 16, 24, 22, 658652)),
        ),
    ]
