# Generated by Django 4.0.3 on 2022-05-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enlistmentbuddyapp', '0012_classmodel_islocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='copypaste',
            field=models.TextField(null=True),
        ),
    ]
