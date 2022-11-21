from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'email', 'username', 'password', 'created_time']


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Following
        fields = ['user_id_follower', 'user_id_followed', 'time']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'user_id', 'created_time', 'title', 'modified_time', 'title', 'content', 'is_reply_to',
                  'visibility']


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikeDislike
        fields = ['post_id', 'user_id', 'time', 'like_dislike']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'post_id', 'user_id', 'created_time', 'modified_time', 'content', 'is_reply_to']


class ChildCommentSerializer(serializers.ModelSerializer):
    is_reply_to = serializers.PrimaryKeyRelatedField(read_only=True)
    parent_comment = CommentSerializer()

    class Meta:
        model = models.Comment
        fields = ['id',
                  'post_id',
                  'user_id',
                  'created_time',
                  'modified_time',
                  'content',
                  'is_reply_to',
                  'parent_comment']

    def validate(self, data):
        if data['is_reply_to'] is not None:
            if data['is_reply_to'] != data['parent_comment']['post_id']:
                raise serializers.ValidationError('Parent comment belongs to a different post')


class LikeDislikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikeDislikeComment
        fields = ['post_id', 'user_id', 'time', 'like_dislike']
