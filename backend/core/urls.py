from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('quest_description', views.get_quest_description, name='quest_description'),
    path('quest_long_description/<int:pk>', views.get_quest_long_description_by_id, name='quest_long_description'),
    path('quest/<int:pk>', views.get_quest, name='quest'),
]