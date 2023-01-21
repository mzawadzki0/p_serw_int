from django.db import models


# Create your models here.

class Following(models.Model):
    user_id_follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='follower')
    user_id_followed = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ('time',)
        unique_together = ('user_id_follower', 'user_id_followed')


class Post(models.Model):
    class PostVisibility(models.TextChoices):
        PUBLIC = 'P'
        FOLLOWERS = 'F'

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500)
    visibility = models.CharField(max_length=1, choices=PostVisibility.choices, default=PostVisibility.PUBLIC)
    is_reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='child_posts')


    class Meta:
        ordering = ('created_time',)

    def __str__(self):
        return str(self.created_time) + '\n' + self.user.username + '\n' + self.title + '\n' + self.content


class LikeDislike(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    like_dislike = models.CharField(max_length=1, choices=LikeDisl.choices, default=LikeDisl.LIKE)

    class Meta:
        ordering = ('time',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=300)
    is_reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child_comments')

    class Meta:
        ordering = ('created_time',)

    def __str__(self):
        return str(self.created_time) + '\n' + self.user.username + '\n' + self.content


class LikeDislikeComment(models.Model):
    class LikeDisl(models.TextChoices):
        LIKE = 'L'
        DISLIKE = 'D'

    post = models.OneToOneField(Comment, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    like_dislike = models.CharField(max_length=1, choices=LikeDisl.choices, default=LikeDisl.LIKE)

    class Meta:
        ordering = ('time',)
