# Generated by Django 4.1.6 on 2023-03-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_alter_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='username'),
        ),
    ]
