# Generated by Django 2.2.8 on 2020-01-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0005_list_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='title',
            new_name='name',
        ),
    ]
