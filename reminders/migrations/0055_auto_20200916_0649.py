# Generated by Django 3.1.1 on 2020-09-16 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0054_auto_20200915_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remindAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 21, 6, 49, 5, 663025)),
        ),
    ]