# Generated by Django 4.0.4 on 2022-05-23 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='rank',
        ),
    ]