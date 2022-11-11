from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    created_time = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    user_id_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    user_id_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('user_id_follower', 'user_id_followed'))


class Post(models.Model):
    class PostVisibility(models.TextChoices):
        PUBLIC = 'P'
        FOLLOWERS = 'F'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500)
    is_reply_to = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    visibility = models.CharField(max_length=1, choices=PostVisibility.choices, default=PostVisibility.PUBLIC)

class LikeDislike(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    post_id = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    like_dislike = models.CharField(max_length=1, choices=LikeDisl.choices, default=LikeDisl.LIKE)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=300)
    is_reply_to = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, default=None, blank=True)

class LikeDislikeComment(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    post_id = models.OneToOneField(Comment, on_delete=models.CASCADE, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    like_dislike = models.CharField(max_length=1, choices=LikeDisl.choices, default=LikeDisl.LIKE)
