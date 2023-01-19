from rest_framework import serializers
from . import models
import django.contrib.auth.password_validation as pw_validation
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username']
        read_only_fields = ['pk', 'username']


class PrivateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'username', 'password']
        read_only_fields = ['pk']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        try:
            pw_validation.validate_password(data['password'])
        except pw_validation.ValidationError as exception:
            raise exception
        return data


class FollowingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Following
        fields = ['user_id_follower', 'user_id_followed', 'time']
        read_only_fields = ['time']


class PostCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Post
        fields = ['user_id', 'title', 'content', 'visibility']

    def create(self, validated_data):
        # stackoverflow
        def _user(obj):
            request = self.context.get('request', None)
            if request:
                return request.user

        post = super().create(validated_data)
        post.user_id = _user.pk


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = models.Post
        fields = ['id', 'user', 'created_time', 'title', 'modified_time', 'content', 'is_reply_to',
                  'visibility']
        read_only_fields = ['id', 'user', 'created_time', 'modified_time']


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LikeDislike
        fields = ['post_id', 'user_id', 'time', 'like_dislike']
        read_only_fields = ['like_dislike']


class ParentCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'post_id']
        read_only_fields = ['id', 'post_id']


class CommentSerializer(serializers.ModelSerializer):
    is_reply_to = ParentCommentSerializer()
    username = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    read_only_fields = ['id', 'created_time', 'modified_time']

    class Meta:
        model = models.Comment
        fields = ['id',
                  'post_id',
                  'user_id',
                  'created_time',
                  'modified_time',
                  'content',
                  'is_reply_to',
                  'username']

    def validate(self, data):
        if data['is_reply_to'] is not None:
            if data['post_id'] != data['is_reply_to']['post_id']:
                raise serializers.ValidationError('Parent comment belongs to a different post')
            if data['id'] == data['is_reply_to']['id']:
                raise serializers.ValidationError('Comment cannot reply to itself')
        return data


class LikeDislikeCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LikeDislikeComment
        fields = ['post_id', 'user_id', 'time', 'like_dislike']
        read_only_fields = ['time']
