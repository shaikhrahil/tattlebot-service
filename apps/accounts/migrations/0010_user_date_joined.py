# Generated by Django 3.2.7 on 2021-09-13 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 15, 20, 59, 498195)),
        ),
    ]
