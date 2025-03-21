# Generated by Django 5.0.3 on 2025-03-21 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.CharField(blank=True, max_length=10, null=True)),
                ('death_date', models.CharField(blank=True, max_length=10, null=True)),
                ('contribution', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_profiles', to='category.category')),
            ],
        ),
    ]
