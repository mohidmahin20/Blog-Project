# Generated by Django 4.2.9 on 2024-06-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
    ]
