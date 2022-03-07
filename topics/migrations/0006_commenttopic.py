# Generated by Django 3.2.11 on 2022-02-22 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0005_delete_commenttopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_for', models.SlugField(max_length=200)),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
