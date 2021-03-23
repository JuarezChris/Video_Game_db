from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_games),
    path('home_page', views.home_page),
    path('new', views.new_page),
    path('add_video_game', views.add_video_game),
    path('details_page/<int:game_id>', views.details_page),
    path('edit_page/<int:game_id>', views.edit_page),
    path('delete/<int:game_id>', views.destroy),
    path('update_my_video_game/<int:game_id>', views.update_my_video_game)
]