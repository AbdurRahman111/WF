# Generated by Django 4.1.7 on 2023-03-03 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FA_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=256, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='news_image/')),
                ('category', models.CharField(blank=True, choices=[('NEVER PLAYED', 'NEVER PLAYED'), ('PLAY SOMETIMES', 'PLAY SOMETIMES'), ('PLAY A LOT', 'PLAY A LOT'), ('WILDCATS', 'WILDCATS')], max_length=256, null=True)),
                ('subcategory', models.CharField(blank=True, choices=[('GET INSPIRED', 'GET INSPIRED'), ('FOOTBALL STORIES', 'FOOTBALL STORIES'), ('FOOTBALL FITNESS', 'FOOTBALL FITNESS')], max_length=256, null=True)),
                ('Description', models.TextField(blank=True, max_length=256, null=True)),
                ('video_link', models.TextField(blank=True, max_length=256, null=True)),
                ('News_Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 3, 19, 31, 5, 30618))),
            ],
            options={
                'verbose_name_plural': 'FA',
            },
        ),
    ]
