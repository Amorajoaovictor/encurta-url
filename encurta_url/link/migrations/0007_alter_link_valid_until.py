# Generated by Django 5.0.6 on 2024-07-20 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0006_alter_link_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 19, 6, 43, 33, 310950, tzinfo=datetime.timezone.utc)),
        ),
    ]
