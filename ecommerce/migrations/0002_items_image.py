# Generated by Django 5.0.2 on 2025-04-14 02:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Pictures/'),
            preserve_default=False,
        ),
    ]
