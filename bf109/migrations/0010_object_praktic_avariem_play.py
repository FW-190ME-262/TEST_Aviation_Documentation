# Generated by Django 5.0.7 on 2024-08-29 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bf109', '0009_object_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='praktic_avariem_play',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bf109.praktic_avariem_play'),
            preserve_default=False,
        ),
    ]
