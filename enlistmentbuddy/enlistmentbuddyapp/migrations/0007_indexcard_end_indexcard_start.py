# Generated by Django 4.0.3 on 2022-03-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enlistmentbuddyapp', '0006_remove_indexcard_end_remove_indexcard_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexcard',
            name='end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='indexcard',
            name='start',
            field=models.TimeField(null=True),
        ),
    ]
