# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.15 on 2018-11-11 02:45
=======
# Generated by Django 1.11.15 on 2018-11-10 03:09
>>>>>>> 14ca6cb368365b15109db2aa2c746c074d63e7bd
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]