# Generated by Django 4.1.2 on 2022-11-28 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_reply_to',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='twitter2.comment'),
        ),
    ]
