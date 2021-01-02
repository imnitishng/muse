# Generated by Django 3.1.2 on 2020-12-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_auto_20201024_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('artist', models.CharField(max_length=2000)),
                ('album', models.CharField(max_length=2000)),
                ('spotify_id', models.CharField(max_length=2000)),
                ('art', models.URLField(max_length=2000)),
                ('lyrics', models.CharField(max_length=20000)),
            ],
        ),
    ]