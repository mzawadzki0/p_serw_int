from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import *
from .serializers import *


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    name = 'user-list'
    search_fields = ['^username']
    filter_fields = ['created_time']
    ordering_fields = ['created_time']


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    search_fields = ['title', 'content']
    filter_fields = ['user_id', 'created_time', 'title', 'content']
    ordering_fields = ['created_time']


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    name = 'post-create'


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    search_fields = ['^username']
    ordering_fields = ['created_time']


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
