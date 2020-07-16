# Generated by Django 3.0.8 on 2020-07-16 18:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('proof', django.contrib.postgres.fields.jsonb.JSONField()),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField()),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
