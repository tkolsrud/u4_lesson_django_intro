# Generated by Django 5.0.3 on 2024-03-25 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='tunr.artist')),
            ],
        ),
    ]
