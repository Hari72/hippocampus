# Generated by Django 3.0.3 on 2020-03-12 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0017_auto_20200311_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remind_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 21, 40, 7, 693060)),
        ),
    ]
