# Generated by Django 2.2.8 on 2020-01-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20191229_1356'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='recent',
            field=models.ManyToManyField(related_name='recent', to='movies.Movie'),
        ),
    ]
