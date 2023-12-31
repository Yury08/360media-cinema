# Generated by Django 4.1.7 on 2023-08-03 09:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user_dislike',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user_like',
        ),
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='reviews_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
