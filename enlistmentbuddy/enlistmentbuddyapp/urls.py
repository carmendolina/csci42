from django.urls import path

#import
from .views import index, index_card_view

#insert urls here
urlpatterns = [
    path('', index, name='index'),
    path('index_card', index_card_view, name='index_card')
    #path("questboard_create", QuestboardCreate, name="questboard_create"),
    #path("questboard_update/<int:pk>", QuestboardUpdate, name="questboard_update"),
    #path("questpage/<int:pk>", QuestPage, name="questpage"),
    
]