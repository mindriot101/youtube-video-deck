# Generated by Django 2.2.7 on 2019-11-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("subscriptions", "0011_auto_20191104_1626")]

    operations = [
        migrations.AddField(
            model_name="video",
            name="url",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        )
    ]
