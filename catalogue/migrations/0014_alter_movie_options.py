# Generated by Django 5.0.7 on 2024-07-16 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_movie_movie_modification_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-movie_creation_date'], 'verbose_name': 'película', 'verbose_name_plural': 'películas'},
        ),
    ]
