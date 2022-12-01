from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UserList.as_view()),
    path('posts', views.PostList.as_view()),
    path('posts/add', views.PostCreate.as_view()),
    path('comments', views.CommentList.as_view()),
    path('comments/add', views.CommentCreate.as_view()),

    # path('', views.index, name='index'),
]
