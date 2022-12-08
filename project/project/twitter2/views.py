from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import *
from .serializers import *
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    name = 'user-list'
    search_fields = ['^username']
    filterset_fields = ['created_time']
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
    filterset_fields = ['user_id__username', 'created_time', 'modified_time', 'is_reply_to']
    ordering_fields = ['created_time']


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    name = 'post-create'


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    search_fields = ['^username', 'content']
    filterset_fields = ['created_time', 'modified_time']
    filter_fields = ['post_id', 'is_reply_to']
    ordering_fields = ['created_time']


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer


class OrederFilter(FilterSet):

