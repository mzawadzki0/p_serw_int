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
        fields = ['id', 'user_id', 'created_time', 'title', 'modified_time', 'title', 'content', 'is_reply_to', 'visibility']

class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikeDislike
        fields = ['post_id', 'user_id', 'time', 'like_dislike']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'post_id', 'user_id', 'created_time', 'modified_time', 'content', 'is_reply_to']

    def validate_reply_to(self, post_id, comment_id):
        # is_reply_to nie może być comment_id z innym post_id
        pass

class LikeDislikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikeDislikeComment
        fields = ['post_id', 'user_id', 'time', 'like_dislike']
