# Generated by Django 3.1.4 on 2020-12-07 19:47

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_nr_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="nr_dlikes",
            field=models.IntegerField(default=0),
        ),
    ]