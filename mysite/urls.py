from django.contrib import admin
from django.urls import path,include
from mysite import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login,name='login'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.logout,name='logout'),
    path('profile_update', views.profile_update,name='profile_update'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('post_form/', views.post_form,name='post_form'),
    path('view_post/', views.view_post,name='view_post'),
    path('update_post/<int:id>/', views.update_post,name='update_post'),
    path('delete_post/<int:id>/', views.delete_post,name='delete_post'),
    path('review/', views.review,name='review'),
    
]