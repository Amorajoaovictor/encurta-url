# Generated by Django 5.0.6 on 2024-07-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_link_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='urlEncurtada',
            field=models.URLField(auto_created=True, blank=True, editable=False),
        ),
    ]
