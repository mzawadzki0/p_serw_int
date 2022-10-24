from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=80)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    created_datetime = models.DateTimeField()

class Following(models.Model):
    user_id_follower = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_followed = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

class Post(models.Model):
    class PostVilibility(models.TextChoices):
        PUBLIC = 'P'
        FOLLOWERS = 'F'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500)
    is_reply_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    visibility = models.CharField(max_length=1, choices=PostVisibility.choices, default=PostVisibility.PUBLIC)

class LikeDislike(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, unique=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    like_dislike = models.TextChoices(max_length=1, choices=LikeDisl.choices, default=LikeDislike.LIKE)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    content = models.CharField(max_length=300)
    is_reply_to = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)

class LikeDislikeComment(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Comment, unique=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    like_dislike = models.TextChoices(max_length=1, choices=LikeDisl.choices, default=LikeDislike.LIKE)
