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


class FollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Following
        fields = ['user_id_follower', 'user_id_followed', 'time']
        read_only_fields = ['time', 'user_id_follower']

    def create(self, validated_data):
        follow_create = models.Following(
            user_id_follower=self.context['request'].user,
            user_id_followed=validated_data['user_id_followed']
        )


class LikeDislikeCommentSerializer(serializers.HyperlinkedModelSerializer):
    comment = serializers.HyperlinkedRelatedField(view_name='comment-detail', queryset=models.Comment.objects.all())
    class Meta:
        model = models.LikeDislikeComment
        fields = ['comment', 'user', 'time', 'like_dislike']
        read_only_fields = ['time', 'user']

    def create(self, validated_data):
        reaction_create = models.LikeDislikeComment(
            comment=validated_data['comment'],
            user=self.context['request'].user,
            like_dislike=validated_data['like_dislike']
        )
        reaction_create.save()
        return reaction_create


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    is_reply_to = serializers.PrimaryKeyRelatedField(queryset=models.Comment.objects.all(), allow_null=True)
    comment_reactions = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Comment
        fields = ['id',
                  'post',
                  'user',
                  'created_time',
                  'modified_time',
                  'content',
                  'is_reply_to',
                  'child_comments',
                  'comment_reactions']
        read_only_fields = ['id', 'user', 'created_time', 'modified_time', 'child_comments', 'comment_reactions']

    def create(self, validated_data):
        comment_create = models.Comment(
            post=validated_data['post'],
            user=self.context['request'].user,
            content=validated_data['content'],
            is_reply_to=validated_data['is_reply_to']
        )
        comment_create.save()
        return comment_create

    # Edytuj tylko treść
    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.save()
        return instance

    def validate(self, data):
        # Odpowiedź na komentarz pod postem innym niż ten, do którego należy self
        if data['is_reply_to'] is not None:
            if data['post'] != data['is_reply_to'].post:
                raise serializers.ValidationError('Parent comment belongs to a different post')
        return data


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name='post-detail', queryset=models.Post.objects.all())
    class Meta:
        model = models.LikeDislike
        fields = ['post', 'user', 'time', 'like_dislike']
        read_only_fields = ['post', 'user']

    def create(self, validated_data):
        reaction_create = models.LikeDislike(
            post=validated_data['post'],
            user=self.context['request'].user,
            like_dislike=validated_data['like_dislike']
        )
        reaction_create.save()
        return reaction_create


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = serializers.StringRelatedField(read_only=True, many=True)
    post_reactions = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Post
        fields = ['id', 'user', 'created_time', 'title', 'modified_time', 'content', 'visibility', 'is_reply_to',
                  'child_posts', 'comments', 'post_reactions']
        read_only_fields = ['id', 'user' 'created_time', 'modified_time', 'child_posts', 'comments', 'post_reactions']

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

    # Edytuj tylko tytuł, treść i widoczność
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.visibility = validated_data['visibility']
        instance.save()
        return instance
