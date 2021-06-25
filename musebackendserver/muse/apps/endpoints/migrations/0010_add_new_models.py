# Generated by Django 3.1.2 on 2021-06-25 12:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0009_remove_unused_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('spotifySeeds', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
        migrations.CreateModel(
            name='UserTrackSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('requestObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectedTracks', to='endpoints.userrequest')),
                ('trackID', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='endpoints.song')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpotifyTrackSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('requestObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectedTracks', to='endpoints.recommendation')),
                ('trackID', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='endpoints.song')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recommendation',
            name='userRequest',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='endpoints.userrequest'),
        ),
    ]