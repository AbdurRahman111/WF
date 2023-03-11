from django.urls import path
from . import views

urlpatterns = [
    path('find_all_FA/', views.find_all_FA, name='find_all_FA'),
    path('create_specific_FA/', views.create_specific_FA, name='create_specific_FA'),
    path('find_all_FA_with_category_subcategory/', views.find_all_FA_with_category_subcategory, name='find_all_FA_with_category_subcategory'),

]
