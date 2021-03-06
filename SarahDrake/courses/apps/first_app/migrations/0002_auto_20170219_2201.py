# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='description',
            fields=[
                ('description', models.TextField(verbose_name=1000)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='course_id', serialize=False, to='first_app.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_id', to='first_app.Course'),
        ),
    ]
