from django.urls import path
from . import views

urlpatterns = [
    path('',views.song_list, name="songs"),
    path('song_detail/<int:pk>/', views.song_detail, name="detail"),
    path('add/<int:pk>/', views.add_note, name="add_note"),
    path('edit/<int:pk>/', views.song_edit, name='edit'),
    path('switch_note/<int:pk_song>/<int:pk_note>/<hole_state>/<int:hole_number>', views.switch_note, name='switch_note'),
    path('delete_note/<int:pk>',views.delete_note, name='delete_note'),
    path('song_edit_comment/<int:pk_song>/<int:pk_note>',views.song_edit_comment, name='song_edit_comment'),
    path('song_edit_title/<int:pk>', views.song_edit_name, name='edit_name'),
    path('song_edit_key/<int:pk>', views.song_edit_key, name='edit_key'),
    path('song_add', views.add_song, name='add_song'),
    path('song_delete/<int:pk>/<delete>', views.delete_song, name='delete_song'),
    path('register/',views.register,name='register'),
]
