from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/create', views.UserCreate.as_view()),
    path('users/edit', views.UserEdit.as_view()),
    path('posts', views.PostList.as_view()),
    path('posts/create', views.PostCreate.as_view()),
    path('posts/edit', views.PostEdit.as_view()),
    path('comments', views.CommentList.as_view()),
    path('comments/create', views.CommentCreate.as_view()),
    path('comments/edit', views.CommentEdit.as_view()),
    path('', views.index, name='index'),
]
