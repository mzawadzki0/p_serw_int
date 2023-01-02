from rest_framework import serializers
from . import models
import django.contrib.auth.password_validation as pw_validation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'created_time']
        read_only_fields = ['username', 'created_time']


class PrivateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'username', 'password', 'created_time']
        read_only_fields = ['created_time']

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


class ParentPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id']
        read_only_fields = ['id']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    is_reply_to = ParentPostSerializer()
    user = serializers.SlugRelatedField(queryset=models.User.objects.all(), slug_field='username')
    class Meta:
        model = models.Post
        fields = ['id', 'user', 'created_time', 'title', 'modified_time', 'title', 'content', 'is_reply_to',
                  'visibility']
        read_only_fields = ['id', 'user', 'created_time', 'modified_time']

    def validate(self, data):
        if data['is_reply_to'] is not None:
            if data['id'] == data['is_reply_to']['id']:
                raise serializers.ValidationError('Post cannot reply to itself')
        return data


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
