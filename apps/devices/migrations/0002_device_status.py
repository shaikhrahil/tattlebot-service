# Generated by Django 3.2.7 on 2021-09-15 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(default='offline', max_length=8, verbose_name=[('active', 'Active'), ('inactive', 'Inactive'), ('online', 'Online'), ('offline', 'Offline')]),
        ),
    ]
