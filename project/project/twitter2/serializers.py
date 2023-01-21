from rest_framework import serializers
from . import models
import django.contrib.auth.password_validation as pw_validation
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'date_joined']
        read_only_fields = ['pk', 'username', 'date_joined']


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


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Post
        fields = [ 'id', 'user', 'created_time', 'title', 'modified_time', 'content',
                  'visibility', 'is_reply_to', 'child_posts', 'comments']
        read_only_fields = ['id', 'user' 'created_time', 'modified_time', 'child_posts', 'comments']
        

    def create(self, validated_data):
        post_create = models.Post(
            user=self.context['request'].user,
            title=validated_data['title'],
            content=validated_data['content'],
            visibility=validated_data['visibility'],
            is_reply_to=validated_data['is_reply_to']
        )
        post_create.save()
        return post_create

    def update(self, instance, validated_data):
        instance = models.Post(
            title=validated_data['title'],
            content=validated_data['content'],
            visibility=validated_data['visibility']
        )
        instance.save()
        return instance


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LikeDislike
        fields = ['post_id', 'user_id', 'time', 'like_dislike']
        read_only_fields = ['like_dislike']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id',
                  'post',
                  'user',
                  'created_time',
                  'modified_time',
                  'content',
                  'is_reply_to',
                  'child_comments']
        read_only_fields = ['id', 'user', 'created_time', 'modified_time', 'child_comments']

    def create(self, validated_data):
        comment_create = models.Comment(
            post=validated_data['post'],
            user=self.context['request'].user,
            content=validated_data['content'],
            is_reply_to=validated_data['is_reply_to']
        )
        comment_create.save()
        return comment_create

    def validate(self, data):
        if data['is_reply_to'] is not None:
            if data['post'] != data['is_reply_to']['post']:
                raise serializers.ValidationError('Parent comment belongs to a different post')


class LikeDislikeCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LikeDislikeComment
        fields = ['post', 'user', 'time', 'like_dislike']
        read_only_fields = ['time']
