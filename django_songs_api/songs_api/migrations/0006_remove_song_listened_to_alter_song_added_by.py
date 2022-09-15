# Generated by Django 4.1.1 on 2022-09-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs_api', '0005_song_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='listened_to',
        ),
        migrations.AlterField(
            model_name='song',
            name='added_by',
            field=models.CharField(max_length=32),
        ),
    ]
