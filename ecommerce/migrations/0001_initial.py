# Generated by Django 5.0.2 on 2025-04-16 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCategory', to='ecommerce.category')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Pictures/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=30)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('category', models.ManyToManyField(related_name='Items', to='ecommerce.category')),
            ],
        ),
    ]
