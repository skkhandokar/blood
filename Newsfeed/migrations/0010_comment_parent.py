# Generated by Django 4.1.6 on 2023-03-31 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0009_post_views_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Newsfeed.comment'),
        ),
    ]
