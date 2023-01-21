# Generated by Django 4.1.2 on 2023-01-19 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='twitter2.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='twitter2.post'),
        ),
    ]