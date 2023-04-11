# Generated by Django 4.1.6 on 2023-03-31 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Newsfeed', '0007_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='post_views', to=settings.AUTH_USER_MODEL),
        ),
    ]