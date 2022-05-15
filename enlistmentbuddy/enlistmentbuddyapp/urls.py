from django.urls import path

#import
from .views import enlistmentbuddy_view

#insert urls here
urlpatterns = [
    #path('', index, name='index'),
    path('', enlistmentbuddy_view, name='home_page'),
    #path("questboard_create", QuestboardCreate, name="questboard_create"),
    #path("questboard_update/<int:pk>", QuestboardUpdate, name="questboard_update"),
    #path("questpage/<int:pk>", QuestPage, name="questpage"),
    
]