# Generated by Django 3.2.11 on 2022-02-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]