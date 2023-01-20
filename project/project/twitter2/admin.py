from django.contrib import admin
from .models import Post, Comment, Following, LikeDislike, LikeDislikeComment


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Following)
admin.site.register(LikeDislike)
admin.site.register(LikeDislikeComment)
