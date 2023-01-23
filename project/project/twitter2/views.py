from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse
from .models import *
from .serializers import *
from .custompermission import *
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def index(request):
    return HttpResponse('<h3>index page</h3><ul><li><a href="users">users</a></li><li><a href="posts">posts</a></li><li><a href="comments">comments</a></li></ul>')


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'create user': reverse(UserCreate.name, request=request),
            'users': reverse(UserList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'post reactions': reverse(LikeDislikeNew.name, request=request),
            'comments': reverse(CommentList.name, request=request),
            'comment reactions': reverse(LikeDislikeCommentNew.name, request=request),
            'follow': reverse(FollowNew.name, request=request)
        })


class UserFilter(FilterSet):
    time_from = DateTimeFilter(field_name='date_joined', lookup_type='gte')
    time_to = DateTimeFilter(field_name='date_joined', lookup_type='lte')

    class Meta:
        model = get_user_model()
        fields=['time_from', 'time_to']


class UserList(generics.ListAPIView):
    Users = get_user_model()
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    search_fields = ['^username']
    filter_class = UserFilter
    ordering_fields = ['time_joined']



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PrivateUserSerializer
    name = 'user-edit'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwner)


class UserCreate(generics.CreateAPIView):
    serializer_class = PrivateUserSerializer
    name= 'user-create'
    permission_classes = (IsAnonymousUser,)


class FollowNew(generics.CreateAPIView):
    queryset = models.Following.objects.all()
    serializer_class = FollowSerializer
    name = 'follow'
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowSerializer
    name = 'follow-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class PostFilter(FilterSet):
    created_time_from = DateTimeFilter(field_name='created_time', lookup_type='gte')
    created_time_to = DateTimeFilter(field_name='created_time', lookup_type='lte')
    modified_time_from = DateTimeFilter(field_name='modified_time', lookup_type='gte')
    modified_time_to = DateTimeFilter(field_name='modified_time', lookup_type='lte')
    user = AllValuesFilter(field_name='user')
    is_reply_to = AllValuesFilter(field_name='is_reply_to')
    class Meta:
        model = Post
        fields=['user',
                'created_time_from',
                'created_time_to',
                'modified_time_from',
                'modified_time_to',
                'is_reply_to']


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    search_fields = ['^user', 'title', 'content']
    filter_class = PostFilter
    ordering_fields = ['created_time']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class LikeDislikeNew(generics.CreateAPIView):
    serializer_class = LikeDislikeSerializer
    name = 'react'
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDislikeDetail(generics.RetrieveDestroyAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer
    name = 'react-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class CommentFilter(FilterSet):
    created_time_from = DateTimeFilter(field_name='created_time', lookup_type='gte')
    created_time_to = DateTimeFilter(field_name='created_time', lookup_type='lte')
    modified_time_from = DateTimeFilter(field_name='modified_time', lookup_type='gte')
    modified_time_to = DateTimeFilter(field_name='modified_time', lookup_type='lte')
    post = AllValuesFilter(field_name='post')
    is_reply_to = AllValuesFilter(field_name='is_reply_to')
    class Meta:
        model = Comment
        fields=['post',
                'created_time_from',
                'created_time_to',
                'modified_time_from',
                'modified_time_to',
                'is_reply_to']


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    search_fields = ['^user', 'content']
    filter_class = CommentFilter
    ordering_fields = ['created_time']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class LikeDislikeCommentNew(generics.CreateAPIView):
    serializer_class = LikeDislikeCommentSerializer
    name = 'react-comment'
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDislikeCommentDetail(generics.RetrieveDestroyAPIView):
    queryset = LikeDislikeComment.objects.all()
    serializer_class = LikeDislikeCommentSerializer
    name = 'react-comment-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)
