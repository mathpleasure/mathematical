# Generated by Django 3.2.11 on 2022-02-22 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20220222_1658'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentTopic',
        ),
    ]