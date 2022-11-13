from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import User, Following, Post, LikeDislike, Comment, LikeDislikeComment
from .serializers import UserSerializer, FollowingSerializer, PostSerializer, LikeDislikeSerializer, CommentSerializer, LikeDislikeCommentSerializer


# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    ordering_fields = ['created_time']

class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    name = 'post-create'
