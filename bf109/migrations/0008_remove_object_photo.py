# Generated by Django 5.0.7 on 2024-08-29 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bf109', '0007_alter_object_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='photo',
        ),
    ]
