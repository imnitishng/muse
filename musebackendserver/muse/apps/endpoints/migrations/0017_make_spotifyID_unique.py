# Generated by Django 3.1.2 on 2021-06-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0016_delete_duplicate_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='spotify_id',
            field=models.CharField(default='undefined', max_length=2000, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='QueryStatus',
        ),
        migrations.DeleteModel(
            name='SongQueryObject',
        ),
    ]
