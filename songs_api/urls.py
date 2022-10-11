from django.urls import path
from . import views

urlpatterns = [
    path('api/songs', views.SongList.as_view(), name='song_list'), 
    path('api/songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'), 
]
