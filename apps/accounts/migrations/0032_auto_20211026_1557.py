# Generated by Django 3.2.7 on 2021-10-26 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20211026_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.AddField(
            model_name='preference',
            name='preference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
