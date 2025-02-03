from django.urls import path
from . import views

urlpatterns = [
    # User-related routes
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    
    # Post-related routes
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/update/', views.update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
