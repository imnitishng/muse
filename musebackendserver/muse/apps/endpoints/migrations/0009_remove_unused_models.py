# Generated by Django 3.1.2 on 2021-06-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0008_querystatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nlpobject',
            name='parent_endpoint',
        ),
        migrations.RemoveField(
            model_name='mlalgorithm',
            name='parent_endpoint',
        ),
        migrations.RemoveField(
            model_name='nlprequest',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='nlprequest',
            name='parent_mlalgorithm',
        ),
        migrations.AddField(
            model_name='nlprequest',
            name='request',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.DeleteModel(
            name='AlgorithmStatus',
        ),
        migrations.DeleteModel(
            name='Endpoint',
        ),
        migrations.DeleteModel(
            name='NLPObject',
        ),
    ]
