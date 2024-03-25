from django.urls import  path
from Musician_Pedia import views


app_name = 'Musician_Pedia'

urlpatterns =[
    path('', views.home, name='home'),
    path('album_form/', views.add_album, name='add_album'),
    path('artist_form/', views.add_artist, name='add_artist'),
    path('list_albums/<int:artist_id>/', views.album_list, name ='album_list'),
    path('update_album/<int:album_id>/<int:artist_id>',views.update_album, name='update_album'),
    path('update_artist/<int:artist_id>/', views.update_artist, name='update_artist'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
]