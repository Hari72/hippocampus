# Generated by Django 3.1.1 on 2020-09-13 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0050_auto_20200819_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 0, 7, 9, 231331)),
        ),
    ]
