# Generated by Django 2.2.8 on 2020-01-05 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_auto_20191229_1356'),
        ('actions', '0003_auto_20200103_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('private', models.BooleanField(default=False)),
                ('official', models.BooleanField(default=False)),
                ('movies', models.ManyToManyField(related_name='movies', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]