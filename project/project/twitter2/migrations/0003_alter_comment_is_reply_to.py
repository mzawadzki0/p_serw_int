# Generated by Django 4.1.2 on 2022-11-28 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter2', '0002_alter_comment_is_reply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_reply_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='twitter2.comment'),
        ),
    ]
