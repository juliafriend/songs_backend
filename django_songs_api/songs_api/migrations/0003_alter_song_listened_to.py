# Generated by Django 4.1.1 on 2022-09-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs_api', '0002_alter_song_listened_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='listened_to',
            field=models.BooleanField(default=True),
        ),
    ]