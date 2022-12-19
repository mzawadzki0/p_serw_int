from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/create', views.UserCreate.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/<int:pk>/edit', views.UserDetail.as_view()),
    path('posts', views.PostList.as_view()),
    path('posts/create', views.PostCreate.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
    path('posts/<int:pk>/edit', views.PostEdit.as_view()),
    path('comments', views.CommentList.as_view()),
    path('comments/create', views.CommentCreate.as_view()),
    path('comments/<int:pk>', views.CommentEdit.as_view()),
    path('comments/<int:pk>/edit', views.CommentEdit.as_view()),
    path('', views.index, name='index'),
]
