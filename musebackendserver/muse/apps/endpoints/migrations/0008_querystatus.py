# Generated by Django 3.1.2 on 2020-12-09 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0007_auto_20201205_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryStatus',
            fields=[
                ('query_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Query_to_QueryStatus', serialize=False, to='endpoints.songqueryobject')),
                ('songids_to_process', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
