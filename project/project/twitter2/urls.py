from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/create', views.UserCreate.as_view(), name=views.UserCreate.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('users/<int:pk>/edit', views.UserEdit.as_view(), name=views.UserEdit.name),
    path('posts', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    path('index', views.index, name='index'),
    path('', views.ApiRoot.as_view())
]
