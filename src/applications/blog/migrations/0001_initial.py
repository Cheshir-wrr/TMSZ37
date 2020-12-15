# Generated by Django 3.1.4 on 2020-12-15 14:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models

import applications.blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True, unique=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(default=applications.blog.models._now),
                ),
                ("nr_likes", models.IntegerField(default=0)),
                ("nr_dlikes", models.IntegerField(default=0)),
                ("nr_views", models.IntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
