# Generated by Django 4.2.6 on 2023-10-24 03:39

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="inf",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("webapp.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]