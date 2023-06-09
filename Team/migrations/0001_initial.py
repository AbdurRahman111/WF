# Generated by Django 4.1.7 on 2023-03-03 13:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_info', '0002_alter_user_information_user_joing_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_player_1_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_2_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_3_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_4_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_5_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_6_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_7_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_8_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_9_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_10_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_11_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_12_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_13_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_14_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_15_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_1_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_2_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_3_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_4_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_5_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_6_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_7_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_8_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_9_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_10_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_active_11_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_substitute_1_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_substitute_2_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_substitute_3_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_player_substitute_4_id_from_Plyer_model', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_Name', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('Team_Owner_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_Total_play_count', models.IntegerField(default=0)),
                ('Win_count', models.IntegerField(default=0)),
                ('Loos_count', models.IntegerField(default=0)),
                ('Drow_count', models.IntegerField(default=0)),
                ('GF', models.IntegerField(default=0)),
                ('GA', models.IntegerField(default=0)),
                ('GD', models.IntegerField(default=0)),
                ('PTS', models.IntegerField(default=0)),
                ('Team_Official_Link', models.CharField(blank=True, max_length=256, null=True)),
                ('Team_Logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Team_Form_Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 3, 19, 27, 42, 402577))),
                ('Manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_info.user_information')),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
    ]
