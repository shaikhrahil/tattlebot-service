# Generated by Django 3.2.7 on 2021-09-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_alter_device_status'),
        ('accounts', '0023_alter_theme_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='devices',
            field=models.ManyToManyField(blank=True, to='devices.Device'),
        ),
    ]
