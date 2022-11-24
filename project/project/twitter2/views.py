from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import *
from .serializers import *


# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    ordering_fields = ['created_time']


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    name = 'post-create'


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    ordering_fields = ['created_time']


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
