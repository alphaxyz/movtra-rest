# Generated by Django 2.2.8 on 2020-01-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
