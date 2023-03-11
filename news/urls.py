from django.urls import path
from . import views

urlpatterns = [
    path('find_all_news/', views.find_all_news, name='find_all_news'),
    path('find_news_with_category/', views.find_news_with_category, name='find_news_with_category'),
    path('create_specific_news/', views.create_specific_news, name='create_specific_news'),
    path('news_category/', views.news_category, name='news_category'),
    path('news_category_create/', views.news_category_create, name='news_category_create'),

]
