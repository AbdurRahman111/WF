# Generated by Django 4.1.7 on 2023-03-03 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Roll', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Operations', 'Operations'), ('Normal User', 'Normal User')], max_length=256, null=True)),
                ('User_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('User_Password', models.CharField(blank=True, max_length=256, null=True)),
                ('User_Email', models.CharField(blank=True, max_length=256, null=True)),
                ('User_Phone', models.CharField(blank=True, max_length=256, null=True)),
                ('User_Joing_Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 3, 19, 27, 16, 903320))),
            ],
            options={
                'verbose_name_plural': 'User information',
            },
        ),
    ]