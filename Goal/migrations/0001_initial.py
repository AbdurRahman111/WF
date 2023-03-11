# Generated by Django 4.1.7 on 2023-03-03 13:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Home_Team_Goal_Count_In_1', models.CharField(blank=True, max_length=256, null=True)),
                ('Way_Team_Goal_Count_In_1', models.CharField(blank=True, max_length=256, null=True)),
                ('Scorer_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Goal_Assist_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Goal_Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 3, 19, 29, 35, 615873))),
                ('Event_for_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_here', to='Event.event_model')),
            ],
            options={
                'verbose_name_plural': 'Goal',
            },
        ),
    ]