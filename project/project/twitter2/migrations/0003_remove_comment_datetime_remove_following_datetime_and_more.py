# Generated by Django 4.1.2 on 2022-11-07 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twitter2', '0002_alter_following_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='following',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='likedislikecomment',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_datetime',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='following',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likedislike',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likedislikecomment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]