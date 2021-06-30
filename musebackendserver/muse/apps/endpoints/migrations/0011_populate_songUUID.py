# Generated by Django 3.1.2 on 2021-06-25 06:01

import uuid
from django.db import migrations, models


def populateUUIDs(apps, schema_editor):
    Songs = apps.get_model('endpoints', 'Songs')

    for row in Songs.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

def depopulateUUIDs(apps, schema_editor):
    Songs = apps.get_model('endpoints', 'Songs')

    for row in Songs.objects.all():
        row.uuid = None
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0010_add_UUIDsongs'),
    ]

    operations = [
        migrations.RunPython(
            populateUUIDs, depopulateUUIDs
        ),
        migrations.AlterField(
            model_name='songs',
            name='uuid',
            field=models.UUIDField(unique=True, serialize=False),
        )
    ]