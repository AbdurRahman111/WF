from django.shortcuts import render, HttpResponse
from .models import Team_Model
from . serializers import Team_Model_serializer
from User_info.serializers import find_manager_information_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q


@csrf_exempt
def find_all_team(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        if Process == 'see_all_team':
            get_spacific_info = Team_Model.objects.all()
            serializer_var = Team_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_team_with_id(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        specific_id = request.POST.get('specific_id')

        if Process == 'find_team_with_id' and specific_id:
            get_spacifi = Team_Model.objects.filter(id = specific_id)
            if get_spacifi:
                get_spacific_info = Team_Model.objects.get(id = specific_id)
                serializer_var = Team_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_team_with_team_name(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        team_name = request.POST.get('team_name')

        if Process == 'find_team_with_team_name' and team_name:
            get_spacifi = Team_Model.objects.filter(Team_Name=team_name)
            if get_spacifi:
                get_spacific_info = Team_Model.objects.get(Team_Name=team_name)
                serializer_var = Team_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')



@csrf_exempt
def find_all_manager(request):
    if request.method == "POST":
        Process = request.POST.get('Process')


        if Process == 'find_all_manager':
            user_info = User_information.objects.filter(User_Roll='Manager')
            serializer_var = find_manager_information_serializer(user_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def create_specific_taem(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        if_admin_then_manager_user_id = request.POST.get('if_admin_then_manager_user_id')


        player_1 = request.POST.get('player_1')
        player_2 = request.POST.get('player_2')
        player_3 = request.POST.get('player_3')
        player_4 = request.POST.get('player_4')
        player_5 = request.POST.get('player_5')
        player_6 = request.POST.get('player_6')
        player_7 = request.POST.get('player_7')
        player_8 = request.POST.get('player_8')
        player_9 = request.POST.get('player_9')
        player_10 = request.POST.get('player_10')
        player_11 = request.POST.get('player_11')
        player_12 = request.POST.get('player_12')
        player_13 = request.POST.get('player_13')
        player_14 = request.POST.get('player_14')
        player_15 = request.POST.get('player_15')

        # active player
        A_player_1 = request.POST.get('A_player_1')
        A_player_2 = request.POST.get('A_player_2')
        A_player_3 = request.POST.get('A_player_3')
        A_player_4 = request.POST.get('A_player_4')
        A_player_5 = request.POST.get('A_player_5')
        A_player_6 = request.POST.get('A_player_6')
        A_player_7 = request.POST.get('A_player_7')
        A_player_8 = request.POST.get('A_player_8')
        A_player_9 = request.POST.get('A_player_9')
        A_player_10 = request.POST.get('A_player_10')
        A_player_11 = request.POST.get('A_player_11')

        # substatute  player
        S_player_1 = request.POST.get('S_player_1')
        S_player_2 = request.POST.get('S_player_2')
        S_player_3 = request.POST.get('S_player_3')
        S_player_4 = request.POST.get('S_player_4')



        Team_Name = request.POST.get('Team_Name')
        Team_Owner_Name = request.POST.get('Team_Owner_Name')

        Team_Total_play_count = request.POST.get('Team_Total_play_count')
        Win_count = request.POST.get('Win_count')
        Loos_count = request.POST.get('Loos_count')
        Drow_count = request.POST.get('Drow_count')
        GF = request.POST.get('GF')
        GA = request.POST.get('GA')
        PTS = request.POST.get('PTS')

        Team_Official_Link = request.POST.get('Team_Official_Link')

        Team_Logo = request.FILES.get('Team_Logo')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):


                    if Process == 'create' and get_user_info.User_Roll =='Admin' and Team_Name and if_admin_then_manager_user_id:
                        manager_info = User_information.objects.filter(id = if_admin_then_manager_user_id)
                        manager_info_one=''
                        if manager_info:
                            manager_info_o = User_information.objects.get(id=if_admin_then_manager_user_id)
                            if manager_info_o.User_Roll == 'Manager':
                                manager_info_one = manager_info_o

                        get_spacific_info = Team_Model(Manager=manager_info_one, Team_player_1_id_from_Plyer_model=player_1, Team_player_2_id_from_Plyer_model=player_2,  Team_player_3_id_from_Plyer_model=player_3, Team_player_4_id_from_Plyer_model=player_4, Team_player_5_id_from_Plyer_model=player_5, Team_player_6_id_from_Plyer_model=player_6, Team_player_7_id_from_Plyer_model=player_7, Team_player_8_id_from_Plyer_model=player_8, Team_player_9_id_from_Plyer_model=player_9, Team_player_10_id_from_Plyer_model=player_10, Team_player_11_id_from_Plyer_model=player_11, Team_player_12_id_from_Plyer_model=player_12, Team_player_13_id_from_Plyer_model=player_13, Team_player_14_id_from_Plyer_model=player_14, Team_player_15_id_from_Plyer_model=player_15, Team_player_active_1_id_from_Plyer_model=A_player_1, Team_player_active_2_id_from_Plyer_model=A_player_2, Team_player_active_3_id_from_Plyer_model=A_player_3, Team_player_active_4_id_from_Plyer_model=A_player_4, Team_player_active_5_id_from_Plyer_model=A_player_5, Team_player_active_6_id_from_Plyer_model=A_player_6, Team_player_active_7_id_from_Plyer_model=A_player_7, Team_player_active_8_id_from_Plyer_model=A_player_8, Team_player_active_9_id_from_Plyer_model=A_player_9, Team_player_active_10_id_from_Plyer_model=A_player_10, Team_player_active_11_id_from_Plyer_model=A_player_11, Team_player_substitute_1_id_from_Plyer_model=S_player_1, Team_player_substitute_2_id_from_Plyer_model=S_player_2, Team_player_substitute_3_id_from_Plyer_model=S_player_3, Team_player_substitute_4_id_from_Plyer_model=S_player_4, Team_Name=Team_Name, Team_Owner_Name=Team_Owner_Name, Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo)
                        get_spacific_info.save()

                        mag = {'massage': 'Data is Created'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'create' and get_user_info.User_Roll =='Manager' and Team_Name:

                        manager_info = User_information.objects.filter(id=get_user_info.id)
                        manager_info_one = ''
                        if manager_info:
                            manager_info_one = User_information.objects.get(id=get_user_info.id)

                        get_spacific_info = Team_Model(Manager=manager_info_one,
                                                       Team_player_1_id_from_Plyer_model=player_1,
                                                       Team_player_2_id_from_Plyer_model=player_2,
                                                       Team_player_3_id_from_Plyer_model=player_3,
                                                       Team_player_4_id_from_Plyer_model=player_4,
                                                       Team_player_5_id_from_Plyer_model=player_5,
                                                       Team_player_6_id_from_Plyer_model=player_6,
                                                       Team_player_7_id_from_Plyer_model=player_7,
                                                       Team_player_8_id_from_Plyer_model=player_8,
                                                       Team_player_9_id_from_Plyer_model=player_9,
                                                       Team_player_10_id_from_Plyer_model=player_10,
                                                       Team_player_11_id_from_Plyer_model=player_11,
                                                       Team_player_12_id_from_Plyer_model=player_12,
                                                       Team_player_13_id_from_Plyer_model=player_13,
                                                       Team_player_14_id_from_Plyer_model=player_14,
                                                       Team_player_15_id_from_Plyer_model=player_15,
                                                       Team_player_active_1_id_from_Plyer_model=A_player_1,
                                                       Team_player_active_2_id_from_Plyer_model=A_player_2,
                                                       Team_player_active_3_id_from_Plyer_model=A_player_3,
                                                       Team_player_active_4_id_from_Plyer_model=A_player_4,
                                                       Team_player_active_5_id_from_Plyer_model=A_player_5,
                                                       Team_player_active_6_id_from_Plyer_model=A_player_6,
                                                       Team_player_active_7_id_from_Plyer_model=A_player_7,
                                                       Team_player_active_8_id_from_Plyer_model=A_player_8,
                                                       Team_player_active_9_id_from_Plyer_model=A_player_9,
                                                       Team_player_active_10_id_from_Plyer_model=A_player_10,
                                                       Team_player_active_11_id_from_Plyer_model=A_player_11,
                                                       Team_player_substitute_1_id_from_Plyer_model=S_player_1,
                                                       Team_player_substitute_2_id_from_Plyer_model=S_player_2,
                                                       Team_player_substitute_3_id_from_Plyer_model=S_player_3,
                                                       Team_player_substitute_4_id_from_Plyer_model=S_player_4,
                                                       Team_Name=Team_Name, Team_Owner_Name=Team_Owner_Name, Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo)
                        get_spacific_info.save()

                        mag = {'massage': 'Data is Created'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    else:
                        HttpResponse('NOT VALID')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')
