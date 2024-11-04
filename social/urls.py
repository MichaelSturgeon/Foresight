# Imported Files and Packages
from django.urls import path
from . import views

# URL Patterns
urlpatterns = [
    path('', views.home, name="home"),
    path('profile_list/', views.profile_list, name="profile_list"),
    path('profile_page/<int:pk>', views.profile_page, name="profile_page"),
    path('edit_post/<int:pk>', views.edit_post, name="edit_post"),
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('profile_page/delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('post_like/<int:pk>', views.post_like, name="post_like"),
    path('follow/<int:pk>', views.follow, name="follow"),
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),
]