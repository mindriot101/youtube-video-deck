# Generated by Django 2.2.7 on 2019-11-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("subscriptions", "0009_video_youtube_id")]

    operations = [
        migrations.AddField(
            model_name="video",
            name="description",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="video",
            name="name",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="video",
            name="thumbnail_url",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
