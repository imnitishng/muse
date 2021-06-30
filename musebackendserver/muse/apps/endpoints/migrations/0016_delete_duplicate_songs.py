# Generated by Django 3.1.2 on 2021-06-27 12:08

from django.db import migrations
from django.db.models import Count

def delete_duplicate_songUUIDs(apps, schema_editor):
    deleted = 0
    Song = apps.get_model('endpoints', 'Song')
    duplicates_spotifyID = Song.objects.values('spotify_id').annotate(Count('id')).order_by().filter(id__count__gt=1)
    total, _ = Song.objects.filter(spotify_id__in=[item['spotify_id'] for item in duplicates_spotifyID]).delete()
    deleted += total
    duplicates_name_artist = Song.objects.values('title', 'main_artist').annotate(uq=Count('title')).order_by().filter(uq__gt=1)
    total, _ = Song.objects.filter(spotify_id__in=[item['title'] for item in duplicates_name_artist]).delete()
    deleted += total
    # print(f'\nTotal deletions: {deleted}')


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0015_SongUUIDtoID'),
    ]

    operations = [
        migrations.RunPython(delete_duplicate_songUUIDs)
    ]