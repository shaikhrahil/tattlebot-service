# Generated by Django 3.2.7 on 2021-09-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20210913_1512"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]
