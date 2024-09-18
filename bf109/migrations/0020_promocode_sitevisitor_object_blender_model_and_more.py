# Generated by Django 5.0.7 on 2024-09-17 06:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bf109', '0019_remove_object_classifikeishen_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('is_for_balance', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='blender_model',
            field=models.FileField(blank=True, null=True, upload_to='blender_models/'),
        ),
        migrations.AddField(
            model_name='object',
            name='drawing',
            field=models.FileField(blank=True, null=True, upload_to='drawings/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='object',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
