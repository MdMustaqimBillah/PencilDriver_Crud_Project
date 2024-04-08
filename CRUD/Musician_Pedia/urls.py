from django.urls import  path
from Musician_Pedia import views


app_name = 'Musician_Pedia'

urlpatterns =[
    path('', views.home, name='home'),
    path('book_form/', views.add_book, name='add_book'),
    path('writer_form/', views.add_writer, name='add_writer'),
    path('book_list/<int:id>/', views.book_list, name ='book_list'),
    path('update_book/<int:book_id>/<int:id>',views.update_book, name='update_book'),
    path('update_writer/<int:id>/', views.update_writer, name='update_writer'),
    path('delete_writer/<int:id>/', views.delete_writer, name='delete_writer'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]