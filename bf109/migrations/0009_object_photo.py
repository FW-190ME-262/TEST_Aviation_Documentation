# Generated by Django 5.0.7 on 2024-08-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bf109', '0008_remove_object_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
