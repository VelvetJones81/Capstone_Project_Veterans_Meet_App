# Generated by Django 4.0.4 on 2022-05-23 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0002_remove_branch_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeteranOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254, verbose_name='User Email')),
                ('address', models.CharField(max_length=125)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=20)),
                ('time_served', models.CharField(max_length=30)),
                ('branch', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='branch.branch')),
            ],
        ),
    ]
