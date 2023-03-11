from django.db import models
from datetime import datetime
# Create your models here.
from User_info.models import User_information





class Team_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Team'

    Manager = models.ForeignKey(User_information, on_delete=models.CASCADE, blank=True, null=True)

    Team_player_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_12_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_13_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_14_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_15_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    Team_player_active_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_active_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    Team_player_substitute_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_substitute_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_substitute_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    Team_player_substitute_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)


    Team_Name = models.CharField(max_length=256, blank=True, null=True, unique=True)

    Team_Owner_Name = models.CharField(max_length=256, blank=True, null=True)
    Team_Total_play_count = models.IntegerField(default=0)

    Win_count = models.IntegerField(default=0)
    Loos_count = models.IntegerField(default=0)
    Drow_count = models.IntegerField(default=0)
    GF = models.IntegerField(default=0)
    GA = models.IntegerField(default=0)
    GD = models.IntegerField(default=0)
    PTS = models.IntegerField(default=0)

    Team_Official_Link = models.CharField(max_length=256, blank=True, null=True)

    Team_Logo = models.ImageField(blank=True, null=True)

    Team_Form_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)



