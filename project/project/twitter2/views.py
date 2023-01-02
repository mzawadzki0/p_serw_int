from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse
from .models import *
from .serializers import *
from .custompermission import *
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


def index(request):
    return HttpResponse('<h3>index page</h3>')


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'posts': reverse(PostList.name, request=request)})


class UserFilter(FilterSet):
    time_from = DateTimeFilter(field_name='time-from', lookup_type='gte')
    time_to = DateTimeFilter(field_name='time-to', lookup_type='lte')

    class Meta:
        model = User
        fields=['time_from', 'time_to']



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    search_fields = ['^username']
    ordering_fields = ['created_time']
    filter_class = UserFilter


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class UserEdit(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PrivateUserSerializer
    name = 'user-edit'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwner)


class UserCreate(generics.CreateAPIView):
    serializer_class = PrivateUserSerializer
    name= 'user-create'


class PostFilter(FilterSet):
    created_time_from = DateTimeFilter(field_name='created_time', lookup_type='gte')
    created_time_to = DateTimeFilter(field_name='created_time', lookup_type='lte')
    modified_time_from = DateTimeFilter(field_name='modified_time', lookup_type='gte')
    modified_time_to = DateTimeFilter(field_name='modified_time', lookup_type='lte')
    user_name = AllValuesFilter(field_name='user_id__username')
    is_reply_to = AllValuesFilter(field_name='is_reply_to')
    class Meta:
        model = User
        fields=['username',
                'created_time_from',
                'created_time_to',
                'modified_time_from',
                'modified_time_to',
                'is_reply_to']


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    search_fields = ['title', 'content']
    filter_class = PostFilter
    ordering_fields = ['created_time']



class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    name = 'post-create'
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class PostEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-edit'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwner)


class CommentFilter(FilterSet):
    created_time_from = DateTimeFilter(field_name='created_time', lookup_type='gte')
    created_time_to = DateTimeFilter(field_name='created_time', lookup_type='lte')
    modified_time_from = DateTimeFilter(field_name='modified_time', lookup_type='gte')
    modified_time_to = DateTimeFilter(field_name='modified_time', lookup_type='lte')
    post_id = AllValuesFilter(field_name='post_id')
    is_reply_to = AllValuesFilter(field_name='is_reply_to')
    class Meta:
        model = User
        fields=['post_id',
                'created_time_from',
                'created_time_to',
                'modified_time_from',
                'modified_time_to',
                'is_reply_to']


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    search_fields = ['^username', 'content']
    filter_class = CommentFilter
    ordering_fields = ['created_time']


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    name = 'comment-create'
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class CommentEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    name = 'comment-edit'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwner)
