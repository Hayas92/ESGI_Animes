from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('anime_list', views.animes, name='anime_list'),
    path('show_vf_animes', views.vf_animes, name='vf'),
    path('show_vostfr_animes', views.vostfr_animes, name='vostfr'),
    path('show_animes_in_progress', views.status_in_progress, name='status_in_progress'),
    path('show_animes_finished', views.status_finished, name='status_finished'),
    path('search_animes', views.search_animes, name='search-animes'),
    path('show_anime/<str:anime_id>/', views.show_anime, name='show_anime')
]
