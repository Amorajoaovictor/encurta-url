# Generated by Django 5.0.6 on 2024-07-20 06:54

import link.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0014_alter_link_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='valid_until',
            field=models.DateTimeField(default=link.models.default_valid_until),
        ),
    ]
