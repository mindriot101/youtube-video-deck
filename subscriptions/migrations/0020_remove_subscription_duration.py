# Generated by Django 2.2.13 on 2020-08-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_subscription_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='duration',
        ),
    ]
