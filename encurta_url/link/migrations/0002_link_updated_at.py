# Generated by Django 5.0.6 on 2024-07-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
