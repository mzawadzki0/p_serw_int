# Generated by Django 4.1.2 on 2022-12-05 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter2', '0003_alter_comment_is_reply_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_time',)},
        ),
        migrations.AlterModelOptions(
            name='likedislike',
            options={'ordering': ('time',)},
        ),
        migrations.AlterModelOptions(
            name='likedislikecomment',
            options={'ordering': ('time',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created_time',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('created_time',)},
        ),
    ]
