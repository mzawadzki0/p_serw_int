from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/create/', views.UserCreate.as_view(), name=views.UserCreate.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('users/<int:pk>/edit/', views.UserEdit.as_view(), name=views.UserEdit.name),
    path('/follow/', views.FollowNew.as_view(), name=views.FollowNew.name),
    path('/follow/<int:pk>/', views.FollowDetail.as_view(), name=views.FollowDetail.name),
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('posts/react/', views.LikeDislikeNew.as_view(), name=views.LikeDislikeNew.name),
    path('posts/react/<int:pk>/', views.LikeDislikeDetail.as_view(), name=views.LikeDislikeDetail.name),
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    path('comments/react/', views.LikeDislikeCommentNew.as_view(), name=views.LikeDislikeCommentNew.name),
    path('comments/react/<int:pk>/', views.LikeDislikeCommentDetail.as_view(), name=views.LikeDislikeCommentDetail.name),
    path('index', views.index, name='index'),
    path('', views.ApiRoot.as_view())
]
